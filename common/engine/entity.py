from typing import Any

import esper

EntityId = int


class Entity:
    def __init__(self):
        self.id: EntityId = esper.create_entity()

    def __add_component(self, component_instance: Any) -> "Entity":
        esper.add_component(self.id, component_instance)
        return self

    def add_components(self, *component_instances: Any) -> "Entity":
        for component_instance in component_instances:
            self.__add_component(component_instance)
        return self
