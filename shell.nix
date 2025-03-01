{ nixpkgs ? import <nixpkgs> {} }:

with nixpkgs;

stdenv.mkDerivation {
  name = "tuebixorg-env";
  buildInputs = [ hugo ];
}

