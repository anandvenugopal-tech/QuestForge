from domain.character import Character

class Warrior(Character):

    def __init__(self, name: str):
        super().__init__(name, health = 120, attack_power = 18)
    
    def speacial_ability(self, target: Character) -> None:
        bonus = int(self.attack_power * 1.5)
        target.take_damage(bonus)
        print(f"{self.name} uses Cleave! {bonus} damage to {target.name}")


class Mage(Character):

    def __init__(self, name: str):
        super().__init__(name, health = 80, attack_power = 10)
        self.mana = 50

    def speacial_ability(self, target: Character):
        cost = 20
        if self.mana < cost:
            print(f"{self.name} doesn't have enough mana!")
            return
        self.mana -= cost
        damage = self.attack_power * 3
        target.take_damage(damage)
        print(f"{self.name} casts Fireball! {damage} damage to {target.name}")


class Rouge(Character):

    def __init__(self, name: str):
        super().__init__(name, health = 90, attack_power = 14)

    def speacial_ability(self, target: Character):
        crit = self.attack_power * 2
        target.take_damage(crit)
        print(f"{self.name} lands a Backstab! {crit} critical damage to {target.name}")

class Cleric(Character):

    def __init__(self, name: str):
        super().__init__(name, health = 100, attack_power = 10)
    
    def speacial_ability(self, target: Character):
        heal_amount = 30
        self._health -= heal_amount
        target.heal(heal_amount)
        print(f"{self.name} uses Heal! {heal_amount} HP restored to {target.name}")
    