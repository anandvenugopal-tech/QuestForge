from abc import ABC, abstractmethod
from domain.inventory import Inventory

class Character(ABC):
    
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self._health = health
        self.__max_health = health
        self.attack_power = attack_power
        self._defense = 0
        self.inventory = Inventory()
    
    @property
    def get_health(self) -> int:
        return self._health

    @property
    def get_defense(self) -> int:
        return self._defense

    @property
    def is_alive(self) -> bool:
        return self._health > 0
    
    def defense(self, amount: int) -> None:
        if amount < 0:
            raise ValueError('Defense can not be negative')
        self._defense += amount

    def take_damage(self, amount:int) -> None:
        if amount < 0:
            raise ValueError("Damage can not be negative")
        
        self._health = max(0, self._health - amount + self.get_defense)
    
    def heal(self, amount:int) -> None:
        self._health = min(self.__max_health, self._health + amount)

    def describe(self) -> str:
        return f"{self.name} has {self._health} HP and {self.attack_power} ATK"

    def attack(self, target: Character) -> None:
        if not self.is_alive:
            return DeadCharacterError(f"{self.name} is dead and can not act")
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    @abstractmethod
    def speacial_ability(self):
         """Every concrete Character MUST define its own special move."""
        raise NotImplementedError

    
    


