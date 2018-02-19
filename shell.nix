{ nixpkgs ? import <nixpkgs> {} }:

with nixpkgs;

stdenv.mkDerivation {
  name = "tuebixorg-env";
  buildInputs = [ (jekyll.override { withOptionalDependencies = true; }) ];
  shellHook = ''
    # Automatically start the server
    exec jekyll serve
  '';
}
