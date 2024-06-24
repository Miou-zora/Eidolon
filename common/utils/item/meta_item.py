from dataclasses import dataclass

MetaItemId = int


@dataclass
class MetaItem:
    """
    MetaItem should be used to give various infos about an item like:
    - Name
    - Description
    - Pattern (MetaItems to use to craft this item)
    - Possible effects
    - Durability
    - Sprite
    - Is stackable
    - ID
    These infos are just examples and can be changed.
    """

    name: str
    # description
    # pattern
    # effects
    # durability
    sprite: str
    # is_stackable
    id: MetaItemId

    def __str__(self):
        return f"MetaItem({self.name})"
