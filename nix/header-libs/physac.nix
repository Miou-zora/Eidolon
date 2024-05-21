{
  mkHeaderLib,
  fetchFromGitHub,
  lib,
}:
mkHeaderLib {
  name = "physac";
  version = "2.5-unstable-2024-05-21";

  src = fetchFromGitHub {
    owner = "victorfisac";
    repo = "Physac";
    rev = "29d9fc06860b54571a02402fff6fa8572d19bd12";
    hash = "sha256-PTlV1tT0axQbmGmJ7JD1n6wmbIxUdu7xho78EO0HNNk=";
  };

  meta = {
    description = "2D physics header-only library for raylib";
    homepage = "https://github.com/victorfisac/Physac";
    license = lib.licenses.mit;
    maintainers = with lib.maintainers; [sigmanificient];
    platforms = lib.platforms.unix;
  };
}
