{
  buildPythonPackage,
  setuptools,
  raylib-python-cffi,
  esper,
  grpcio,
  grpcio-tools,
  pymunk,
}:
buildPythonPackage {
  pname = "eidolon-common";

  version = with builtins;
    head (match ".*(0.0.1).*" (readFile ../setup.cfg));

  pyproject = true;
  build-system = [setuptools];

  src = ./..;
  propagatedBuildInputs =
    [
      grpcio
      grpcio-tools
      pymunk
    ]
    ++ [
      raylib-python-cffi
      esper
    ];
}
