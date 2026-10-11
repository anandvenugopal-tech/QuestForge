from domain.item import Item

class HealthPotion(Item):
    
    def __init__(self, heal_amount: int = 25):
        self.heal_amount = heal_amount

    def apply(self, character: Character) -> str:
        character.heal(self.heal_amount)
        return f"{character.name} drinks a potion and heals {self.heal_amount} HP!"


class Weapon(Item):

    def __init__(self, name: str, bous_attack: int):
        self.name = name
        self.bonus_attack = bonu_attack

    def apply(self, character: Character) -> str:
        character.attack_power += self.bonus_attack
        return f"{character.name} equips {self.name} (+{self.bonus_attack} ATK)"    
    

class Armor(Item):

    def __init__(self, name: str, defense_bonus: int):
        self.name = name
        self.defense_bonus = defense_bonus
    
    def play(self, character: Character):
        character.defence(self.defense_bonus)
        