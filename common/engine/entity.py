from __future__ import annotations

import esper

from common.engine import component

EntityId = int


class Entity:
    def __init__(self) -> None:
        self.id: EntityId = esper.create_entity()

    def add_components(self, *component_instances: component) -> Entity:
        for component_instance in component_instances:
            esper.add_component(self.id, component_instance)
        return self
