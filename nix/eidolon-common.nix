{
  buildPythonPackage,
  setuptools,
  raylib-python-cffi,
  esper,
  pymunk,
  lib,
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
      pymunk
    ]
    ++ [
      raylib-python-cffi
      esper
    ];

  meta = {
    homepage = "https://github.com/Miou-zora/Eidolon";
    license = lib.licenses.gpl3Only;
    maintainers = with lib.maintainers; [sigmanificient];
    platforms = lib.platforms.unix;
  };
}
