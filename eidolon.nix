{
  lib,
  stdenv,
  xmake,
}: let
  build-dir = "build/linux/x86_64/release";
in
  stdenv.mkDerivation {
    name = "eidolon";
    version = "1.0.0";

    src = ./.;

    nativeBuildInputs = [xmake];

    preConfigure = ''
      xmake f  -m release -y \
        --ld=${lib.getExe stdenv.cc} --cc=${lib.getExe stdenv.cc}
    '';

    buildPhase = "xmake b --verbose";

    installPhase = ''
      mkdir -p $out/bin

      install -Dm 755 ${build-dir}/Client $out/bin/Client
      install -Dm 755 ${build-dir}/Server $out/bin/Server
    '';
  }
