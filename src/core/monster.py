# src/core/monsters.py

from typing import Dict, List, Optional


class Monster:
    def __init__(
        self,
        name: str,
        monster_type: str,
        complexity: float,  # сложность
        level: int = 1,
        attributes: Optional[Dict[str, int]] = None,
        hp: Optional[int] = None,
        damage: Optional[str] = None,   # например "1d6+2"
        abilities: Optional[List[str]] = None,
        loot: Optional[List[str]] = None,
    ):
        self.name = name
        self.monster_type = monster_type
        self.complexity = complexity
        self.level = level
        self.attributes = attributes or {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 8,
            "wisdom": 8,
            "charisma": 6
        }

        # HP можно задать или рассчитать
        self.hp = hp if hp is not None else self.calculate_hp()
        self.damage = damage or "1d4"  # базовый урон
        self.abilities = abilities or []
        self.loot = loot or []

    def calculate_hp(self) -> int:
        """Расчёт HP по телосложению"""
        base_hp = 8
        con_mod = (self.attributes["constitution"] - 10) // 2
        return base_hp + con_mod + (self.level - 1) * 4

    def add_ability(self, ability: str):
        self.abilities.append(ability)

    def add_loot(self, item: str):
        self.loot.append(item)

    def __repr__(self):
        return f"<{self.monster_type} {self.name} (Сложность {self.complexity}, ОЗ {self.hp}, Урон {self.damage})>"


# ====== Примеры монстров ======

class Goblin(Monster):
    def __init__(self, name: str = "Гоблин", **kwargs):
        default_attr = {"strength": 8, "dexterity": 14, "constitution": 10,
                        "intelligence": 8, "wisdom": 8, "charisma": 8}
        kwargs.setdefault("attributes", default_attr)
        kwargs.setdefault("damage", "1d6+2")
        kwargs.setdefault("loot", ["Ржавый кинжал"])
        super().__init__(name, "Гоблин", complexity=0.25, **kwargs)


class Orc(Monster):
    def __init__(self, name: str = "Орк", **kwargs):
        default_attr = {"strength": 16, "dexterity": 12, "constitution": 14,
                        "intelligence": 7, "wisdom": 11, "charisma": 10}
        kwargs.setdefault("attributes", default_attr)
        kwargs.setdefault("damage", "1d12+3")
        kwargs.setdefault("loot", ["Боевой топор"])
        super().__init__(name, "Орк", complexity=0.5, **kwargs)


class Dragon(Monster):
    def __init__(self, name: str = "Дракон", **kwargs):
        default_attr = {"strength": 23, "dexterity": 10, "constitution": 21,
                        "intelligence": 16, "wisdom": 15, "charisma": 19}
        kwargs.setdefault("attributes", default_attr)
        kwargs.setdefault("damage", "2d10+6")
        kwargs.setdefault("loot", ["Золото", "Драконья чешуя"])
        super().__init__(name, "Дракон", complexity=1000, **kwargs)


dragon = Dragon()
print(dragon.loot)



# хоба!
# troll = Monster(
#     name="Тролль",
#     monster_type="Гигант",
#     complexity=5,
#     level=3,
#     attributes={"strength": 1800000000, "dexterity": 10, "constitution": 16,
#                 "intelligence": 7, "wisdom": 9, "charisma": 7},
#     hp=84000000000,
#     damage="2d6+4",
#     abilities=["бесмертие", "очень сильная атака"],
#     loot=["лак для волос из мочи дракона", "меч героя"]
# )

# print(troll, troll.loot)