{
  stdenv,
  linkify-it-py,
  myst-parser,
  sphinx,
  sphinxawesome-theme,
  sphinxcontrib-trio,
}:
stdenv.mkDerivation {
  name = "eidolon-docs";
  src = ../../docs;

  nativeBuildInputs = [
    linkify-it-py
    myst-parser
    sphinx
    sphinxawesome-theme
    sphinxcontrib-trio
  ];

  installPhase = ''
    mkdir -p $out/
    cp -R .build/html/* $out/
  '';
}
