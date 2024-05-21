{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    pre-commit-hooks = {
      url = "github:cachix/git-hooks.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    nixpkgs,
    pre-commit-hooks,
  }: let
    defaultSystems = [
      "aarch64-linux"
      "aarch64-darwin"
      "x86_64-darwin"
      "x86_64-linux"
    ];

    forAllSystems = function:
      nixpkgs.lib.genAttrs defaultSystems
      (system: function nixpkgs.legacyPackages.${system});
  in
    {
      formatter = forAllSystems (pkgs: pkgs.alejandra);

      checks = forAllSystems (pkgs: let
        hooks = {
          alejandra.enable = true;
          check-merge-conflicts.enable = true;
          check-shebang-scripts-are-executable.enable = true;
          check-added-large-files.enable = true;
        };
      in {
        pre-commit-check = pre-commit-hooks.lib.${pkgs.system}.run {
          inherit hooks;
          src = ./.;
        };
      });
    }
    // (let
      outputs =
        forAllSystems
        (pkgs: import ./nix {inherit self pkgs;});

      mapVals = f: attr: builtins.mapAttrs (_: f) attr;

      transforms = {
        devShells = out: {default = out.shell;};
        packages = out: out.packages;
      };
    in
      mapVals
      (value: forAllSystems (pkgs: value outputs.${pkgs.system}))
      transforms);
}
