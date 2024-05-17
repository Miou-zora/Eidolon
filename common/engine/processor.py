from typing import TypeVar

from esper import Processor

ProcessorClass = TypeVar("ProcessorClass", bound=Processor)
