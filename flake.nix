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
        deps = with pkgs.python311.pkgs;
          [
            grpcio
            grpcio-tools
            pymunk
          ]
          ++ (with self.packages.${system}; [
            esper
            raylib-python-cffi
            eidolon-common
          ]);
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

        env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
          pkgs.stdenv.cc.cc
          pkgs.glfw
          pkgs.xorg.libX11
          pkgs.libglvnd
        ];

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
          ${venvDir}/bin/pip install -e .
        '';
      };

      packages = {
        default = self.packages.${system}.eidolon-client;

        eidolon-client = pkgs.callPackage ./nix/eidolon-client.nix {
          pyenv = py.env;
        };

        eidolon-common = pkgs.callPackage ./nix/eidolon-common.nix {
          inherit (pkgs.python3Packages) buildPythonPackage grpcio grpcio-tools pymunk setuptools;
          inherit (self.packages.${system}) raylib-python-cffi esper;
        };

        esper = pkgs.callPackage ./nix/esper.nix {
          inherit (pkgs.python3Packages) buildPythonPackage flit-core pytestCheckHook;
        };

        physac = pkgs.callPackage ./nix/header-libs/physac.nix {};
        raygui = pkgs.callPackage ./nix/header-libs/raygui.nix {};

        raylib-python-cffi = pkgs.callPackage ./nix/raylib-python-cffi.nix {
          inherit (self.packages.${system}) physac raygui;
          inherit (pkgs.python3Packages) buildPythonPackage cffi setuptools;
        };
      };
    });
}
