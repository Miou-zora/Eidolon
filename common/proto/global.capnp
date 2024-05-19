@0xec1d412ed82a2db9;

struct Position {
	x @0 :Float64;
	y @1 :Float64;
	z @2 :Float64;
}


interface Inter {
	move @0 (pos :Position) -> (result :Position);
}
