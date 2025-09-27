from typing import Optional


class Spell:
    def __init__(
        self,
        name: str,
        level: int,                 # уровень заклинания
        school: str,                # школа магии
        description: str = "",
        damage: Optional[str] = None,   # урон
        effect: Optional[str] = None,   # эффект
        mana_cost: int = 0              # стоимость маны
    ):
        self.name = name
        self.level = level
        self.school = school
        self.description = description
        self.damage = damage
        self.effect = effect
        self.mana_cost = mana_cost

    def __repr__(self):
        return f"<Заклинание {self.name} (Ур. {self.level}, {self.school})>"


# ====== Примеры заклинаний ======

class Fireball(Spell):
    def __init__(self, **kwargs):
        kwargs.setdefault("level", 3)
        kwargs.setdefault("school", "Огненная магия")
        kwargs.setdefault("description", "Взрыв огня, наносящий урон всем врагам в области.")
        kwargs.setdefault("damage", "8d6")
        kwargs.setdefault("mana_cost", 10)
        super().__init__("Огненный шар", **kwargs)


class HealingWord(Spell):
    def __init__(self, **kwargs):
        kwargs.setdefault("level", 1)
        kwargs.setdefault("school", "Исцеляющая магия")
        kwargs.setdefault("description", "Заклинание, которое восстанавливает здоровье союзнику.")
        kwargs.setdefault("effect", "Восстановить 1d4+модификатор мудрости HP")
        kwargs.setdefault("mana_cost", 4)
        super().__init__("Исцеляющее слово", **kwargs)


class MagicMissile(Spell):
    def __init__(self, **kwargs):
        kwargs.setdefault("level", 1)
        kwargs.setdefault("school", "Чистая энергия")
        kwargs.setdefault("description", "Создаёт магические снаряды, которые всегда попадают в цель.")
        kwargs.setdefault("damage", "3d4+3")  # три снаряда по 1d4+1
        kwargs.setdefault("mana_cost", 5)
        super().__init__("Магическая стрела", **kwargs)

fireball = Fireball()
print(fireball)