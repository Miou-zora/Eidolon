{pkgs}: let
  BuildHeaderLib = src:
    pkgs.callPackage src
    {mkHeaderLib = pkgs.callPackage ./mk-header-lib.nix {};};
in {
  physac = BuildHeaderLib ./physac.nix;
  raygui = BuildHeaderLib ./raygui.nix;
}
