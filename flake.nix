{
  inputs = {
    naersk.url = "github:nix-community/naersk/master";
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    flake-utils,
    naersk,
    nixpkgs,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = (import nixpkgs) {
          inherit system;
        };

        naersk' = pkgs.callPackage naersk {};
        src = ./.;
        bin = naersk'.buildPackage {inherit src;};
      in {
        packages = {
          default = bin;
          check = naersk'.buildPackage {
            inherit src;
            mode = "check";
          };
          test = naersk'.buildPackage {
            inherit src;
            mode = "test";
          };
          clippy = naersk'.buildPackage {
            inherit src;
            mode = "clippy";
          };
          dev = pkgs.writeShellScriptBin "dev" ''
            ${bin}/bin/massoth-tech-rs;
            ${pkgs.lib.getExe pkgs.http-server} ./dist -c-1;
          '';
        };

        devShell = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [rustc cargo rustfmt pre-commit rustPackages.clippy http-server];
          RUST_SRC_PATH = pkgs.rustPlatform.rustLibSrc;
        };
      }
    );
}
