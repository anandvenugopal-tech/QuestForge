from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric
from domain.battle import run_special_round, total_party_damage
from pattern.creational import CharacterFactory, EnemyBuilder
from domain.items import HealthPotion
from pattern.singleton import GameManager


from domain.classes import Warrior
from pattern.decorators import RageBuff, PoisonDebuff


hero = Warrior("Bram")
print(f"Base attack: {hero.attack_power}")


# Wrap the hero in a RageBuff
raging_hero = RageBuff(hero)
print(f"Raging attack: {raging_hero.attack_power}")


# Wrap the raging hero in a PoisonDebuff (Stacking!)
poisoned_raging_hero = PoisonDebuff(raging_hero)
print(f"Still raging attack: {poisoned_raging_hero.attack_power}")


# Trigger the poison
print(poisoned_raging_hero.tick())
print(f"HP after poison: {poisoned_raging_hero.get_health}")
    

    


    


    