from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric
from domain.battle import run_special_round, total_party_damage
from pattern.creational import CharacterFactory, EnemyBuilder
from domain.items import HealthPotion
from pattern.singleton import GameManager


manager1 = GameManager()
manager1.difficulty = "hard"


# Somewhere else in the code, we try to create a new manager
manager2 = GameManager()


print(f"Manager 2 difficulty: {manager2.difficulty}") 
# Outputs "hard" because manager1 and manager2 are the exact same object!


print(f"Are they the same object? {manager1 is manager2}")
    

    


    


    