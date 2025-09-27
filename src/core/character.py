# src/core/character.py
from typing import Dict, List


class Character:
    def __init__(self, name: str, race: str, char_class: str, level: int = 1, attributes: Dict[str, int] = None):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level
        self.attributes = attributes or {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }
        self.hp = self.calculate_hp()
        self.inventory: List[str] = []
        self.skills: Dict[str, int] = {}
        self.spells: List[str] = []
        self.experience = 0

    def calculate_hp(self) -> int:
        """Вычисление хп по классу и телосложению"""
        base_hp = {
            "Воин": 12,
            "Маг": 6,
            "Плут": 8,
            "Обычный NPC": 4
        }
        con_mod = (self.attributes["constitution"] - 10) // 2
        return base_hp.get(self.char_class, 6) + con_mod

    def level_up(self):
        """Повышение уровня"""
        self.level += 1
        self.hp += (self.calculate_hp() // 2)  # при апе хп растет
        self.experience = 0

    def add_item(self, item: str):
        self.inventory.append(item)

    def learn_skill(self, skill: str, level: int = 1):
        self.skills[skill] = level

    def learn_spell(self, spell: str):
        if self.char_class == "Маг":
            self.spells.append(spell)

    def __repr__(self):
        return f"<{self.char_class} {self.name} (Lvl {self.level}, HP {self.hp})>"


# ====== Игровые классы персонажей ======

class Warrior(Character):
    def __init__(self, name: str, race: str, attributes: Dict[str, int] = None):
        super().__init__(name, race, "Воин", attributes=attributes)


class Mage(Character):
    def __init__(self, name: str, race: str, attributes: Dict[str, int] = None):
        super().__init__(name, race, "Маг", attributes=attributes)


class Rogue(Character):
    def __init__(self, name: str, race: str, attributes: Dict[str, int] = None):
        super().__init__(name, race, "Плут", attributes=attributes)


# ====== NPC ======

class Trader(Character):
    def __init__(self, name: str, race: str = "Человек"):
        super().__init__(name, race, "Торговец", level=1, attributes={"strength": 8, "dexterity": 8, "constitution": 8, "intelligence": 12, "wisdom": 10, "charisma": 14})


class Merchant(Character):
    def __init__(self, name: str, race: str = "Человек"):
        super().__init__(name, race, "Продавец", level=1, attributes={"strength": 7, "dexterity": 9, "constitution": 9, "intelligence": 11, "wisdom": 10, "charisma": 15})