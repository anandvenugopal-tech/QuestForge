from domain.character import Character




if __name__ == "__main__":

    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 30, 5)

    print(hero.describe())
    print(goblin.describe())

    hero.attack(goblin)
    print(goblin.describe())

    hero.health = -50
    print(hero.get_health)
    