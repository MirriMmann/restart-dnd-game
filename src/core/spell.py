from typing import Optional, List


class Spell:
    def __init__(
        self,
        name: str,
        level: int,
        school: str,                # школа магии
        description: str = "",
        damage: Optional[str] = None,
        effect: Optional[str] = None,
        mana_cost: int = 0,         # стоимость маны
        duration: str = "Мгновенно",   # время действия
        area: str = "Цель: 1 существо", # область действия
        allowed_classes: Optional[List[str]] = None,  # кто может использовать
    ):
        self.name = name
        self.level = level
        self.school = school
        self.description = description
        self.damage = damage
        self.effect = effect
        self.mana_cost = mana_cost
        self.duration = duration
        self.area = area
        self.allowed_classes = allowed_classes or ["Маг", "Чародей", "Колдун"]

    def can_cast(self, char_class: str) -> bool:
        """Проверяет, может ли персонаж этого класса использовать заклинание"""
        return char_class in self.allowed_classes

    def __repr__(self):
        return (f"<Заклинание {self.name} (Ур. {self.level}, {self.school}, "
                f"Длительность: {self.duration}, Область: {self.area})>")


# ====== Примеры заклинаний ======

class Fireball(Spell):
    def __init__(self, **kwargs):
        kwargs.setdefault("level", 3)
        kwargs.setdefault("school", "Огненная магия")
        kwargs.setdefault("description", "Взрыв огня, наносящий урон всем врагам в области.")
        kwargs.setdefault("damage", "8d6")
        kwargs.setdefault("mana_cost", 10)
        kwargs.setdefault("duration", "Мгновенно")
        kwargs.setdefault("area", "Радиус 6 метров")
        kwargs.setdefault("allowed_classes", ["Маг", "Колдун", "Чародей"])
        super().__init__("Огненный шар", **kwargs)


class HealingWord(Spell):
    def __init__(self, **kwargs):
        kwargs.setdefault("level", 1)
        kwargs.setdefault("school", "Исцеляющая магия")
        kwargs.setdefault("description", "Заклинание, которое восстанавливает здоровье союзнику.")
        kwargs.setdefault("effect", "Восстановить 1d4+модификатор мудрости HP")
        kwargs.setdefault("mana_cost", 4)
        kwargs.setdefault("duration", "Мгновенно")
        kwargs.setdefault("area", "Один союзник в пределах 18 метров")
        kwargs.setdefault("allowed_classes", ["Жрец", "Паладин"])
        super().__init__("Исцеляющее слово", **kwargs)


class MagicMissile(Spell):
    def __init__(self, **kwargs):
        kwargs.setdefault("level", 1)
        kwargs.setdefault("school", "Чистая энергия")
        kwargs.setdefault("description", "Создаёт магические снаряды, которые всегда попадают в цель.")
        kwargs.setdefault("damage", "3d4+3")  # три снаряда по 1d4+1
        kwargs.setdefault("mana_cost", 5)
        kwargs.setdefault("duration", "Мгновенно")
        kwargs.setdefault("area", "До 3 целей в пределах 36 метров")
        kwargs.setdefault("allowed_classes", ["Маг", "Чародей"])
        super().__init__("Магическая стрела", **kwargs)


# ====== Пример использования ======
fireball = Fireball()
print(fireball)
print(fireball)
