import esper
import pyray

import pymunk  # Import pymunk..

space = pymunk.Space()  # Create a Space which contain the simulation
space.gravity = 0, -981  # Set its gravity

body = pymunk.Body()  # Create a Body
body.position = 50, 100  # Set the position of the body

poly = pymunk.Poly.create_box(body)  # Create a box shape and attach to body
poly.mass = 10  # Set the mass on the shape
space.add(body, poly)  # Add both body and shape to the simulation

print_options = pymunk.SpaceDebugDrawOptions()  # For easy printing

for _ in range(100):  # Run simulation 100 steps in total
    space.step(0.02)  # Step the simulation one step forward
    space.debug_draw(print_options)

from dataclasses import dataclass as component


@component
class Position:
    x: float = 0.0
    y: float = 0.0


player = esper.create_entity()
esper.add_component(player, Position(x=5, y=5))
print(player)


def main():
    print("Hello world!: From client")
    pyray.init_window(800, 450, "Hello")
    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.WHITE)
        pyray.draw_text("Hello world from client", 190, 200, 20, pyray.VIOLET)
        pyray.end_drawing()
    pyray.close_window()


if __name__ == "__main__":
    main()
