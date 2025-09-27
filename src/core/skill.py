# src/core/skills.py

from typing import Dict, Optional


class Skill:
    def __init__(
        self,
        name: str,
        description: str,
        base_level: int = 1,
        max_level: int = 5,
        requirements: Optional[Dict[str, int]] = None,  # требования к характеристикам
    ):
        self.name = name
        self.description = description
        self.level = base_level
        self.max_level = max_level
        self.requirements = requirements or {}

    def can_learn(self, attributes: Dict[str, int]) -> bool:
        """Проверяет, подходит ли персонаж по требованиям"""
        for attr, value in self.requirements.items():
            if attributes.get(attr, 0) < value:
                return False
        return True

    def level_up(self):
        """Повышение уровня навыка"""
        if self.level < self.max_level:
            self.level += 1

    def __repr__(self):
        return f"<Навык {self.name} (Ур. {self.level}/{self.max_level})>"


# ====== Примеры навыков ======

class Stealth(Skill):
    def __init__(self):
        super().__init__(
            name="Скрытность",
            description="Позволяет прятаться и бесшумно передвигаться.",
            base_level=1,
            max_level=5,
            requirements={"ловкость": 12}
        )


class Swordsmanship(Skill):
    def __init__(self):
        super().__init__(
            name="Фехтование",
            description="Улучшает владение мечом, повышает урон.",
            base_level=1,
            max_level=10,
            requirements={"сила": 12}
        )


class ArcaneKnowledge(Skill):
    def __init__(self):
        super().__init__(
            name="Магические знания",
            description="Позволяет изучать и понимать заклинания.",
            base_level=1,
            max_level=7,
            requirements={"интеллект": 14}
        )


# ====== Пример использования ======

iceball = Skill(
    name="Ледяной шар",
    description="Создаёт ледяной шар замедляющий врагов",
    base_level=8,
    max_level=5,
    requirements={"интеллект": 13, "мудрость": 10}
)
print(iceball)