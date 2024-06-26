{
  mkHeaderLib,
  fetchFromGitHub,
  lib,
}:
mkHeaderLib {
  name = "raygui";
  version = "4.0-unstable-2024-05-21";

  src = fetchFromGitHub {
    owner = "raysan5";
    repo = "raygui";
    rev = "25c8c65a6e5f0f4d4b564a0343861898c6f2778b";
    hash = "sha256-1qnChZYsb0e5LnPhvs6a/R5Ammgj2HWFNe9625sBRo8=";
  };

  meta = {
    description = "A simple and easy-to-use immediate-mode gui library";
    homepage = "https://github.com/raysan5/raygui";
    license = lib.licenses.zlib;
    maintainers = with lib.maintainers; [sigmanificient];
    platforms = lib.platforms.unix;
  };
}
