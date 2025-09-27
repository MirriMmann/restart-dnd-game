from typing import Optional


class Item:
    def __init__(
        self,
        name: str,
        item_type: str,          
        description: str = "",    
        value: int = 0,              
        weight: float = 0.0,         
        damage: Optional[str] = None, 
        defense: Optional[int] = None, 
        effect: Optional[str] = None 
    ):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.value = value
        self.weight = weight
        self.damage = damage
        self.defense = defense
        self.effect = effect

    def __repr__(self):
        return f"<{self.item_type}: {self.name} (цена {self.value}, вес {self.weight})>"


# ====== Примеры предметов ======

class Sword(Item):
    def __init__(self, name: str = "Меч", **kwargs):
        kwargs.setdefault("item_type", "Оружие")
        kwargs.setdefault("description", "Обычный стальной меч.")
        kwargs.setdefault("value", 10)
        kwargs.setdefault("weight", 3.0)
        kwargs.setdefault("damage", "1d8+2")
        super().__init__(name, **kwargs)


class Shield(Item):
    def __init__(self, name: str = "Щит", **kwargs):
        kwargs.setdefault("item_type", "Броня")
        kwargs.setdefault("description", "Деревянный щит.")
        kwargs.setdefault("value", 8)
        kwargs.setdefault("weight", 5.0)
        kwargs.setdefault("defense", 2)  # бонус к защите
        super().__init__(name, **kwargs)


class HealingPotion(Item):
    def __init__(self, name: str = "Зелье лечения", **kwargs):
        kwargs.setdefault("item_type", "Зелье")
        kwargs.setdefault("description", "Восстанавливает здоровье.")
        kwargs.setdefault("value", 5)
        kwargs.setdefault("weight", 0.5)
        kwargs.setdefault("effect", "Восстановит 10 HP")
        super().__init__(name, **kwargs)


Healing = HealingPotion()
print(Healing, Healing.effect)





# hammer = Item(
#     name = "Боевой молот",
#     item_type = "Дробящее",
#     description="Тяжёлый молот с металлической головкой.",
#     value=15,
#     weight=4.0,
#     damage="50",
#     defense="сила +2",
#     effect="оглушение"
# )
# print(hammer, hammer.damage + " урона" )
