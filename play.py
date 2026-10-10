from domain.character import Character
from domain.classes import Warrior, Mage, Rouge, Cleric
from domain.battle import run_special_round, total_party_damage




if __name__ == "__main__":

    party = [Warrior('Bram'), Mage('Sylla'), Rouge('Kade')]
    dummy = Warrior('Training Dummy')

    for member in party:
        member.speacial_ability(dummy)
        print(f"Dummy HP: {dummy.get_health}\n")

    total_party_damage(party, dummy)
    print(f"Dummy HP: {dummy.get_health}\n")
    

    


    


    