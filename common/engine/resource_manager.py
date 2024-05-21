from .resource import Resource

from typing import TypeVar

GenericResource = TypeVar("GenericResource", bound=Resource)

class ResourceManager:
    class ResourceNotFoundError(Exception):
        def __init__(self, resource):
            super().__init__(f"Resource {resource} not found")

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
