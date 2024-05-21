from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .resource import Resource

from typing import TypeVar

GenericResource = TypeVar("GenericResource", bound=Resource)

class ResourceManager:
    class ResourceNotFoundError(Exception):
        def __init__(self, resource: type[Resource]):
            super().__init__("Resource %s not found", resource.__name__)

    def __init__(self):
        self.resources: list[Resource] = []

    def get_resource_safe(self, resource: type[Resource]):
        for res in self.resources:
            if isinstance(res, resource):
                return res
        return None

    def get_resource(self, resource: type[GenericResource]) -> GenericResource:
        for res in self.resources:
            if isinstance(res, resource):
                return res
        raise ResourceManager.ResourceNotFoundError(resource)

    def insert_resource(self, resource):
        self.resources.append(resource)
