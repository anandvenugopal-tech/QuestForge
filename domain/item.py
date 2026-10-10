from abc import ABC, abstractmethod
from domain.character import Character

class Item(ABC):

    @abstractmethod
    def apply(self, character: Character):
        """Apply this item's effect to a character; return a description string."""
