{
  self,
  pkgs,
}: let
  py = pkgs.python310;

  selectPythonPackages = ps:
    [
      ps.pytest
      ps.pymunk
      ps.sphinx
    ]
    ++ (with self.packages.${pkgs.system}; [
      esper
      raylib-python-cffi
      eidolon-common
    ]);

  pyenv = py.withPackages selectPythonPackages;

  pkgs' = self.packages.${pkgs.system};
in {
  shell = pkgs.mkShell rec {
    name = "Eidolon";

    env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
      pkgs.glfw
      pkgs.xorg.libX11
      pkgs.libglvnd
    ];

    inputsFrom = pkgs.lib.attrsets.attrValues self.packages.${pkgs.system};
    packages = with pkgs; [
      black
      pyenv
      pyenv.pkgs.venvShellHook
      python3Packages.nox
    ];

    venvDir = "venv";
    shellHook = ''
      ${self.checks.${pkgs.system}.pre-commit-check.shellHook}

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

      docs = py.pkgs.callPackage ./docs {};
    }
    // {
      default = pkgs'.eidolon-client;

      eidolon-client =
        pkgs.callPackage ./eidolon-client.nix
        {inherit pyenv;};

      setup-cfg =
        pkgs.callPackage ./generate_setup_config.nix {};
    }
    // (import ./header-libs {inherit pkgs;});
}
