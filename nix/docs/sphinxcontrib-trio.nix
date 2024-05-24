{
  lib,
  buildPythonPackage,
  fetchPypi,
  sphinx,
  setuptools,
  wheel,
}:
# Credits: https://github.com/NixOS/nixpkgs/pull/296880
buildPythonPackage rec {
  pname = "sphinxcontrib-trio";
  version = "1.1.2";
  pyproject = true;

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-nxupwdWWW1NOhSWNi2d92U6bGpoukYuFzNQlkFlrR8A=";
  };

  build-system = [
    setuptools
    wheel
  ];

  propagatedBuildInputs = [
    sphinx
  ];

  pythonImportsCheck = ["sphinxcontrib_trio"];

  meta = with lib; {
    description = "Make Sphinx better at documenting Python functions and methods";
    homepage = "https://pypi.org/project/sphinxcontrib-trio/";
    license = with licenses; [mit asl20];
    maintainers = with maintainers; [sigmanifiient];
  };
}
