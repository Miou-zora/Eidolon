{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";

    pre-commit-hooks = {
      url = "github:cachix/git-hooks.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    esper = {
      url = "github:benmoran56/esper?ref=v3.2";
      flake = false;
    };
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    pre-commit-hooks,
    esper,
  }:
    flake-utils.lib.eachSystem ["x86_64-linux"]
    (system: let
      pkgs = nixpkgs.legacyPackages.${system};

      py = {
        env = pkgs.python311.withPackages (p: py.deps);
        deps = with pkgs.python311.pkgs; [
          grpcio
          grpcio-tools
          (self.packages.${system}.esper)
          pymunk
        ];
      };
    in rec {
      formatter = pkgs.alejandra;

      checks = let
        hooks = {
          alejandra.enable = true;
          check-merge-conflicts.enable = true;
          check-shebang-scripts-are-executable.enable = true;
          check-added-large-files.enable = true;
        };
      in {
        pre-commit-check = pre-commit-hooks.lib.${system}.run {
          inherit hooks;
          src = ./.;
        };
      };

      devShells.default = pkgs.mkShell rec {
        name = "Eidolon";

        env.LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";

        packages = with pkgs;
          [
            py.env
            py.env.pkgs.venvShellHook
          ]
          ++ (with python312Packages; [
            black
          ])
          ++ [pkgs.raylib];

        venvDir = "venv";
        shellHook = ''
          ${checks.pre-commit-check.shellHook}

          SOURCE_DATE_EPOCH=$(date +%s)

          if [ -d "${venvDir}" ]; then
            echo "Skipping venv creation, '${venvDir}' already exists"
          else
            echo "Creating new venv environment in path: '${venvDir}'"
            ${py.env.python.interpreter} -m venv "${venvDir}"
          fi

          source "${venvDir}/bin/activate"
          ${venvDir}/bin/pip install -r requirements.txt
        '';

        postVenvCreation = ''
          pip install -r ./requirements.txt
          pip install -e .
        '';
      };

      packages = let
        mk-libheader = {
          name,
          version,
          src,
          description,
          pcfile,
        }:
          pkgs.stdenv.mkDerivation rec {
            inherit name version src;

            dontBuild = true;
            installPhase = ''
              mkdir -p $out/{include,lib/pkgconfig}

              cp $src/src/physac.h $out/include/${name}.h

              cat <<EOF > $out/lib/pkgconfig/${name}.pc
              prefix=$out
              includedir=$out/include

              Name: ${name}
              Version: ${version}
              Cflags: -I"{includedir}"
              EOF
            '';
          };
      in {
        esper = pkgs.python311Packages.buildPythonPackage {
          pname = "esper";
          version = "3.2";
          pyproject = true;

          src = esper;

          build-system = [py.env.pkgs.flit-core];
          doCheck = false;
        };

        physac = mk-libheader {
          name = "physac";
          version = "2.5-unstable-20240518";

          src = pkgs.fetchFromGitHub {
            owner = "victorfisac";
            repo = "Physac";
            rev = "29d9fc06860b54571a02402fff6fa8572d19bd12";
            hash = "sha256-PTlV1tT0axQbmGmJ7JD1n6wmbIxUdu7xho78EO0HNNk=";
          };
        };

        raygui = mk-libheader {
          name = "raygui";
          version = "4.0-unstable-25c8";

          src = pkgs.fetchFromGitHub {
            owner = "raysan5";
            repo = "raygui";
            rev = "25c8c65a6e5f0f4d4b564a0343861898c6f2778b";
            hash = "sha256-1qnChZYsb0e5LnPhvs6a/R5Ammgj2HWFNe9625sBRo8=";
          };
        };

        pyray = pkgs.python311Packages.buildPythonPackage rec {
          pname = "pyray";
          version = "5.0.0.2";

          src = pkgs.fetchFromGitHub {
            owner = "electronstudio";
            repo = "raylib-python-cffi";
            rev = "refs/tags/v${version}";
            hash = "sha256-DlnZRJZ0ZnkLii09grA/lGsJHPUYrbaJ55BVWJ8JzfM=";
          };

          build-system = [
            pkgs.python311Packages.setuptools
            pkgs.python311Packages.cffi
          ];

          patches = [./fix-pyray-builder.patch];
          nativeBuildInputs = [pkgs.pkg-config];

          buildInputs = [
            pkgs.python311
            pkgs.glfw
            pkgs.libffi
            pkgs.raylib
            packages.physac
            packages.raygui
          ];
        };
      };
    });
}
