from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeVar
    from .resource import Resource

    GenericResource = TypeVar("GenericResource", bound=Resource)

import logging

logger = logging.getLogger(__name__)


class ResourceManager:
    class ResourceNotFoundError(Exception):
        def __init__(self, resource: type[Resource]):
            super().__init__("Resource %s not found", resource.__name__)

    def __init__(self):
        self.resources: dict[int, Resource] = {}

    def get_resource_safe(self, resource: type[Resource]):
        return self.resources.get(id(resource), None)

    def get_resource(self, resource: type[GenericResource]) -> GenericResource:
        return self.resources[id(resource)]

    def insert_resource(self, resource: GenericResource):
        self.resources[id(resource.__class__)] = resource
