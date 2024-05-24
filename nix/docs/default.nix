{
  stdenv,
  linkify-it-py,
  myst-parser,
  sphinx,
}:
stdenv.mkDerivation {
  name = "eidolon-docs";
  src = ../../docs;

  nativeBuildInputs = [
    linkify-it-py
    myst-parser
    sphinx
  ];

  installPhase = ''
    mkdir -p $out/
    cp -R .build/html/* $out/
  '';
}
