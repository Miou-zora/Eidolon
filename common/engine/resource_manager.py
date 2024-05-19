from .resource import Resource


class ResourceManager:
    class ResourceNotFoundError(Exception):
        def __init__(self, resource):
            super().__init__(f"Resource {resource} not found")

    def __init__(self):
        self.resources: list[Resource] = []

    def get_resource_safe(self, resource):
        for res in self.resources:
            if isinstance(res, resource):
                return res
        return None

    def get_resource(self, resource):
        for res in self.resources:
            if isinstance(res, resource):
                return res
        raise ResourceManager.ResourceNotFoundError(resource)

    def add_resource(self, resource):
        self.resources.append(resource)
