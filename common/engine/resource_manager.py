from .resource import Resource


class ResourceManager:
    def __init__(self):
        self.resources: list[Resource] = []

    def get_resource(self, resource):
        for res in self.resources:
            if isinstance(res, resource):
                return res
        return None

    def add_resource(self, resource):
        self.resources.append(resource)
