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

      packages = {
        esper = pkgs.python311Packages.buildPythonPackage {
          pname = "esper";
          version = "3.2";
          pyproject = true;

          src = esper;

          build-system = [py.env.pkgs.flit-core];
          doCheck = false;
        };
      };
    });
}
