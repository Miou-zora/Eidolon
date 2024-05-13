import esper

from dataclasses import dataclass as component


@component
class Position:
    x: float = 0.0
    y: float = 0.0


player = esper.create_entity()
esper.add_component(player, Position(x=5, y=5))
print(player)


def main():
    print("Hello world!")


if __name__ == "__main__":
    main()
