{
  stdenvNoCC,
  pyenv,
  lib,
}:
stdenvNoCC.mkDerivation {
  name = "client";
  src = ../client;

  buildPhase = ''
    cp -r $src lib

    chmod +w lib
    rm -rf lib/__main__.py
  '';

  installPhase = ''
    mkdir -p $out
    cp -r lib $out/lib

    echo -e "#!${pyenv}/bin/python" \
      | cat - $src/__main__.py > $out/lib/__main__.py

    mkdir -p $out/bin

    ln -s $out/lib/__main__.py $out/bin/client
    chmod +x $out/bin/client
  '';

  meta = {
    description = "A simple client showcase for eidolon";
    homepage = "https://github.com/Miou-zora/Eidolon";
    license = lib.licenses.gpl2Only;
    maintainers = with lib.maintainers; [sigmanificient];
    platforms = lib.platforms.unix;
  };
}
