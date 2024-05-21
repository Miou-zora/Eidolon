{
  pkgs,
  py,
  pyenv,
  system,
  self,
}: let
  pkgs' = self.packages.${system};
in
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
  // (import ./header-libs {inherit pkgs;})
