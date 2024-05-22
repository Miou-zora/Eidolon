#!/usr/bin/env python3
import pathlib
import sys

from typing import Final

EXIT_KO: Final[int] = 1


def has_correct_message(msg: str) -> bool:
    print(f"Commit message:\n{msg}")

    verb, *words = msg.split()
    report = {
        "  " in msg: "double space!",
        msg.startswith(" ") or msg.endswith(" "): "leading or trailling space",
        verb[0].islower(): "verb is not capitalized",
        any(map(verb.endswith, {"ed", "ing", "s"})): "use imperative tense",
        msg.endswith("."): "message should not end with a period",
        len(words) < 2: "include at least 3 words",
    }.get(True)

    if report is None:
        return True

    print(report)
    return False


def main():
    if len(sys.argv) != 2:
        return EXIT_KO

    message = pathlib.Path(sys.argv[1]).read_text()
    return not has_correct_message(message)


if __name__ == "__main__":
    sys.exit(main())
