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
    flake-utils.lib.eachSystem ["x86_64-linux"] (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in
        {
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
        }
        // (let
          outputs =
            import ./nix
            {inherit self pkgs system;};
        in {
          devShells.default = outputs.shell;
          packages = outputs.packages;
        })
    );
}
