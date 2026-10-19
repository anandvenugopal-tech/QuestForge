from abc import ABC, abstractmethod
from domain.character import Character


class Usable(ABC):

    @abstractmethod
    def apply(self, character: Character):
        """Apply a consumable item's effect."""
        pass

class Equippable(ABC):

    @abstractmethod
    def apply(self, character: Character):
        """Equip an item for persistent stat changes."""
        pass