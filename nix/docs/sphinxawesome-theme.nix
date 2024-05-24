{
  buildPythonPackage,
  fetchPypi,
  lib,
  poetry-core,
  sphinx,
  beautifulsoup4,
}:
buildPythonPackage rec {
  pname = "sphinxawesome_theme";
  version = "5.1.4";
  pyproject = true;

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-OwikuKJrPo4vNaud/9JToYYJePV6Kew8izYbr/qKTtQ=";
  };

  build-system = [poetry-core];
  dependencies = [
    sphinx
    beautifulsoup4
  ];

  prePatch = ''
    substituteInPlace pyproject.toml \
      --replace-fail "^7.2,<7.3" ">=7.3"
  '';

  meta = {
    description = "Awesome Sphinx Theme";
    homepage = "https://sphinxawesome.xyz/";
    license = lib.licenses.mit;
    maintainers = with lib.maintainers; [sigmanificient];
  };
}
