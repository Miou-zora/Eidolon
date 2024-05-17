import esper
from typing import Any

EntityId = int


class Entity:
    def __init__(self):
        self.id: EntityId = esper.create_entity()

    def add_component(self, component_instance: Any) -> None:
        esper.add_component(self.id, component_instance)
