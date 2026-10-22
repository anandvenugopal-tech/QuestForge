from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric
from domain.battle import run_special_round, total_party_damage
from pattern.creational import CharacterFactory, EnemyBuilder
from domain.items import HealthPotion


player = CharacterFactory.create("mage", "Sylla")


# Using Builder
boss = (EnemyBuilder("Dragon")
        .with_health(500)
        .with_attack(50)
        .with_loot(HealthPotion())
        .build())


print(f"Created {player.name} (HP: {player.get_health})")
print(f"Created {boss.name} (HP: {boss.get_health})")
    

    


    


    