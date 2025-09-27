# src\core\character.py

from typing import Dict, List, Optional


class Character:
    def __init__(
        self,
        name: str,
        race: str,
        char_class: str,
        level: int = 1,
        attributes: Optional[Dict[str, int]] = None,
        hp: Optional[int] = None,
        experience: int = 0,
        inventory: Optional[List[str]] = None,
        skills: Optional[Dict[str, int]] = None,
        spells: Optional[List[str]] = None,
    ):
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

        # либо берём переданный hp, либо считаем
        self.hp = hp if hp is not None else self.calculate_hp()
        self.experience = experience
        self.inventory = inventory or []
        self.skills = skills or {}
        self.spells = spells or []

    def calculate_hp(self) -> int:
        """Вычисление хп по классу и телосложению"""
        base_hp = {
            "Воин": 12,
            "Маг": 6,
            "Плут": 8,
            "Торговец": 5,
            "Продавец": 5,
            "NPC": 4
        }
        con_mod = (self.attributes["constitution"] - 10) // 2
        return base_hp.get(self.char_class, 6) + con_mod + (self.level - 1) * 5

    def level_up(self):
        """Повышение уровня"""
        self.level += 1
        self.hp += 5 + (self.attributes["constitution"] - 10) // 2
        self.experience = 0

    def add_item(self, item: str):
        self.inventory.append(item)

    def learn_skill(self, skill: str, level: int = 1):
        self.skills[skill] = level

    def learn_spell(self, spell: str):
        if self.char_class == "Маг":
            self.spells.append(spell)

    def __repr__(self):
        return f"<{self.char_class} {self.name} (Lvl {self.level}, HP {self.hp},)>"

# ====== NPC ======

class Trader(Character):
    def __init__(self, name: str, race: str = "Человек", **kwargs):
        default_attr = {"strength": 8, "dexterity": 8, "constitution": 8,
                        "intelligence": 12, "wisdom": 10, "charisma": 14}
        kwargs.setdefault("attributes", default_attr)
        super().__init__(name, race, "Торговец", **kwargs)


class Merchant(Character):
    def __init__(self, name: str, race: str = "Человек", **kwargs):
        default_attr = {"strength": 7, "dexterity": 9, "constitution": 9,
                        "intelligence": 11, "wisdom": 10, "charisma": 15}
        kwargs.setdefault("attributes", default_attr)
        super().__init__(name, race, "Продавец", **kwargs)



#вот для удобства
# hero = Character(
#     name="Тестовый",
#     race="Эльф",
#     char_class="Воин",
#     level=3,
#     attributes={},
#     hp=50,
#     inventory=["Меч", "Щит"],
#     skills={"Атака": 2, "Защита": 1},
#     spells=[]
# )

# print(hero)
# print("Инвентарь:", hero.attributes)
