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

      selectPythonPackages = ps:
        [
          ps.grpcio
          ps.grpcio-tools
          ps.pymunk
        ]
        ++ (with self.packages.${system}; [
          esper
          raylib-python-cffi
          eidolon-common
        ]);

      pyenv = pkgs.python311.withPackages selectPythonPackages;
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

        inputsFrom = pkgs.lib.attrsets.attrValues self.packages.${system};
        packages = with pkgs; [
          black
          pyenv
          pyenv.pkgs.venvShellHook
        ];

        venvDir = "venv";
        shellHook = ''
          ${checks.pre-commit-check.shellHook}

          SOURCE_DATE_EPOCH=$(date +%s)

          if [ -d "${venvDir}" ]; then
            echo "Skipping venv creation, '${venvDir}' already exists"
          else
            echo "Creating new venv environment in path: '${venvDir}'"
            ${pyenv.python.interpreter} -m venv "${venvDir}"
          fi

          source "${venvDir}/bin/activate"
          ${venvDir}/bin/pip install -r requirements.txt
          ${venvDir}/bin/pip install -e .
        '';
      };

      packages = let
        ps = pkgs.python311.pkgs;
      in
        {
          eidolon-common = ps.callPackage ./nix/eidolon-common.nix {
            inherit (self.packages.${system}) raylib-python-cffi esper;
          };

          esper = ps.callPackage ./nix/esper.nix {};

          raylib-python-cffi = ps.callPackage ./nix/raylib-python-cffi.nix {
            inherit (self.packages.${system}) physac raygui;
          };
        }
        // {
          default = self.packages.${system}.eidolon-client;

          eidolon-client = pkgs.callPackage ./nix/eidolon-client.nix {
            pyenv = pyenv;
          };
        }
        // (import ./nix/header-libs {inherit pkgs;});
    });
}
