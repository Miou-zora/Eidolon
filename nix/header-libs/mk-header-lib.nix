{stdenvNoCC}: {
  name,
  version,
  src,
  meta,
}:
stdenvNoCC.mkDerivation {
  inherit name version src meta;

  dontBuild = true;
  installPhase = ''
    mkdir -p $out/{include,lib/pkgconfig}

    cp $src/src/${name}.h $out/include/${name}.h

    cat <<EOF > $out/lib/pkgconfig/${name}.pc
    prefix=$out
    includedir=$out/include
    Name: ${name}
    Description: ${meta.description}
    URL: ${meta.homepage}
    Version: ${version}
    Cflags: -I"{includedir}"
    EOF
  '';
}
