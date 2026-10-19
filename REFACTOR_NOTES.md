# SOLID refactor notes (Levels 1–7)

Concrete “before” snippets from QuestForge Levels 1–7, and the “after” that maps each SOLID letter. These examples are meant to drop into the architecture write-up.

---

## S — Single Responsibility

**Problem:** `Character` owned stats, combat, *and* bag logic. Adding items meant editing the fighter.

**Before (Level 1 `domain/character.py` — combat plus mutating another unit’s HP in the same class):**

```python
def attack(self, target: Character) -> None:
    target.health -= self.attack_power
    print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

def heal(self, target: Character, amount: int) -> None:
    target.health += amount
```

**After (Level 6):** `Character` keeps combat state; a composed `Inventory` owns add / use / list. `domain/battle.py` owns the round loop.

```python
self.inventory = Inventory()
```

```python
class Inventory:
    def add(self, item): ...
    def use(self, index: int, target: Character): ...
```

---

## O — Open/Closed

**Problem:** A new class would have required new `if isinstance(...)` branches in the battle loop.

**Before (the shape Level 4 would have needed without polymorphism):**

```python
for member in party:
    if isinstance(member, Warrior):
        member.speacial_ability(dummy)
    elif isinstance(member, Mage):
        member.speacial_ability(dummy)
    elif isinstance(member, Rouge):
        member.speacial_ability(dummy)
```

**After (Level 4 `domain/battle.py`):** the loop is closed for modification; new classes only add `speacial_ability`.

```python
def run_special_round(attacker: Character, defender: Character) -> None:
    attacker.speacial_ability(defender)

def total_party_damage(party: list[Character], target: Character):
    for member in party:
        member.attack(target)
```

---

## L — Liskov Substitution

**Problem:** `Mage.speacial_ability` silently no-op’d on low mana, while Warrior/Rogue always applied damage. Callers using `Character` could not trust the same contract.

**Before (Level 4 `domain/classes.py`):**

```python
def speacial_ability(self, target: Character):
    cost = 20
    if self.mana < cost:
        print(f"{self.name} doesn't have enough mana!")
        return
    self.mana -= cost
    ...
```

**After (Level 7):** same method, fail by raising a domain error so any `Character` either acts or signals failure.

```python
if self.mana < cost:
    raise InsuffientManaError(
        f"{self.name} needs {cost} mana, has {self.mana}"
    )
```

---

## I — Interface Segregation

**Problem:** One fat `Item` ABC forced potions, weapons, and armor onto the same `apply` contract (Armor even grew a unused `play` method).

**Before (Level 5 `domain/item.py` / Level 6 `domain/Items.py`):**

```python
class Item(ABC):
    @abstractmethod
    def apply(self, character: Character):
        """Apply this item's effect to a character; return a description string."""

class Armor(Item):
    def play(self, character: Character):
        character.defence(self.defense_bonus)
```

**After:** split into role interfaces; consumables implement `Usable`, gear implements `Equippable`.

```python
class Usable(ABC):
    @abstractmethod
    def apply(self, character: Character):
        """Apply a consumable item's effect."""

class Equippable(ABC):
    @abstractmethod
    def apply(self, character: Character):
        """Equip an item for persistent stat changes."""
```

```python
class HealthPotion(Usable): ...
class Weapon(Equippable): ...
class Armor(Equippable): ...
```

---

## D — Dependency Inversion

**Problem:** `Inventory` depended on a concrete `Weapon` type, so potions and armor could not be stored without changing `Inventory`.

**Before (Level 6–7 `domain/inventory.py`):**

```python
def add(self, item: Weapon) -> None:
    self._items.append(item)
```

**After:** high-level inventory depends on the item abstractions, not a concrete class.

```python
from domain.item import Usable, Equippable

def add(self, item: Usable | Equippable) -> None:
    self._items.append(item)
```
