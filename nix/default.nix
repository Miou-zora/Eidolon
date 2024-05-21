{
  self,
  pkgs,
  system,
}: let
  py = pkgs.python311;

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

  pyenv = py.withPackages selectPythonPackages;

  pkgs' = self.packages.${system};
in {
  shell = pkgs.mkShell rec {
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
      ${self.checks.${system}.pre-commit-check.shellHook}

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
  packages =
    {
      eidolon-common = py.pkgs.callPackage ./eidolon-common.nix {
        inherit (pkgs') raylib-python-cffi esper;
      };

      esper = py.pkgs.callPackage ./esper.nix {};

      raylib-python-cffi = py.pkgs.callPackage ./raylib-python-cffi.nix {
        inherit (pkgs') physac raygui;
      };
    }
    // {
      default = pkgs'.eidolon-client;

      eidolon-client =
        pkgs.callPackage ./eidolon-client.nix
        {inherit pyenv;};
    }
    // (import ./header-libs {inherit pkgs;});
}
