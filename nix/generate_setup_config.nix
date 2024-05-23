{stdenvNoCC}:
stdenvNoCC.mkDerivation {
  name = "setup.cfg";
  src = ../.;

  buildPhase = ''
    subpackages="$(                                     \
      find $src/common -type d -not -name "__pycache__" \
        | cut -d '/' -f 5-                              \
        | tr '/' '.'                                    \
        | sort                                          \
        | xargs -i echo '    {}')"

    export subpackages="''${subpackages:4}"
    eval "echo \"''$(cat $src/setup.cfg.in)\" " | tee setup.cfg
  '';

  installPhase = "cp setup.cfg $out";
}
