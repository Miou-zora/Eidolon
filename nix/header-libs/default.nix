{pkgs, ...}: {
  physac = pkgs.callPackage ./physac.nix {};
  raygui = pkgs.callPackage ./raygui.nix {};
}
