# EIDOLON ENGINE

Eidolon is a game engine written in python using esper as ECS framework. It is designed to be simple and easy to use.

## How to use

There is a simple example:

```python
import logging

import esper

from common.engine import component
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers import UnitTimeProvider
from common.resources.time_providers.time_provider import TimeProvider

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


@component
class Position:
    x: float
    y: float

    def __str__(self) -> str:
        return f"Position({self.x},{self.y})"


@component
class Name:
    name: str

    def __str__(self) -> str:
        return f"{self.name}"


class LogProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        # This is how you get resources
        time_provider: UnitTimeProvider = r.get_resource(TimeProvider)
        if time_provider is None:
            raise NotImplemented(
                f"Resource not found: UnitTimeProvider:{time_provider}"
            )

        # Simple logging
        logger.info(f"Elapsed time: {time_provider.get_elapsed_time()}")
        for ent, (pos, name) in esper.get_components(Position, Name):
            logger.debug(f"{name}: {pos}")


def run():
    engine: Engine = Engine()

    engine.register_resource(UnitTimeProvider())
    engine.add_processor(LogProcessor())

    entity: Entity = Entity()
    entity.add_component(Position(32, 64))
    entity.add_component(Name("First Entity"))
    entity2: Entity = Entity()
    entity2.add_component(Position(69, 42))
    entity2.add_component(Name("Second Entity"))
    engine.run()


if __name__ == "__main__":
    run()
```