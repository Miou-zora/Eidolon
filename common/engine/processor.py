import esper
from typing import TypeVar

Processor = esper.Processor
ProcessorClass = TypeVar("ProcessorClass", bound=Processor)
