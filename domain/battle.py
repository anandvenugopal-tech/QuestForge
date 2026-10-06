from domain.character import Character

def run_special_round(attacker: Character, defender: Character) -> None:
    
    attacker.speacial_ability(defender)


def total_party_damage(party: list[Character], target: Character):

    for member in party:
        member.attack(target)

