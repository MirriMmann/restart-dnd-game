# src\core\character.py

import random
from typing import Dict, List, Optional


class Character:
    def __init__(
        self,
        name: str,
        race: str,
        char_class: str,
        level: int = 1,
        strength: int = 10,
        dexterity: int = 10,
        constitution: int = 10,
        intelligence: int = 10,
        wisdom: int = 10,
        charisma: int = 10,
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
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hp = hp if hp is not None else self.calculate_hp()
        self.experience = experience
        self.inventory = inventory or []
        self.skills = skills or {}
        self.spells = spells or []

    def calculate_hp(self) -> int:
        """Вычисление хп по классу и телосложению с учётом уровня (система кубиков)."""
        base_hp = {
            "Барбар": 12,        # 1d12 + модификатор конституции
            "Бард": 8,           # 1d8 + модификатор конституции
            "Боевой маг": 8,     # 1d8 + модификатор конституции
            "Воин": 10,          # 1d10 + модификатор конституции
            "Друид": 8,          # 1d8 + модификатор конституции
            "Жрец": 8,           # 1d8 + модификатор конституции
            "Колдун": 6,         # 1d6 + модификатор конституции
            "Маг": 6,            # 1d6 + модификатор конституции
            "Монах": 8,          # 1d8 + модификатор конституции
            "Паладин": 10,       # 1d10 + модификатор конституции
            "Плут": 8,           # 1d8 + модификатор конституции
            "Следопыт": 10,      # 1d10 + модификатор конституции
            "Творец": 8,         # 1d8 + модификатор конституции
        }

        base = base_hp.get(self.char_class, 6)
        con_mod = (self.constitution - 10) // 2
        hp = base + con_mod  # базовое значение здоровья с учетом конституции

        # Добавляем здоровье за каждый уровень (1d6, 1d8 или 1d10)
        for _ in range(1, self.level):
            hp += random.randint(1, base) + con_mod  # случайный кубик для уровня + модификатор

        return hp
    
    def calculate_skill_bonus(self, skill: str) -> int:
        """Вычисление бонуса для навыков на основе атрибутов и обученности навыка."""
        
        # Атрибуты, связанные с каждым навыком
        skill_attributes = {
            "Акробатика": "dexterity",       # Ловкость
            "Атлетика": "strength",          # Сила
            "Ловкость рук": "dexterity",     # Ловкость
            "Скрытность": "dexterity",       # Ловкость
            "История": "intelligence",      # Интеллект
            "Магия": "intelligence",        # Интеллект
            "Природа": "intelligence",      # Интеллект
            "Расследование": "intelligence",# Интеллект
            "Религия": "intelligence",      # Интеллект
            "Восприятие": "wisdom",         # Мудрость
            "Выживание": "wisdom",          # Мудрость
            "Медицина": "wisdom",           # Мудрость
            "Проницательность": "wisdom",   # Мудрость
            "Уход за животными": "wisdom", # Мудрость
            "Выступление": "charisma",      # Харизма
            "Запугивание": "charisma",     # Харизма
            "Обман": "charisma",            # Харизма
            "Убеждение": "charisma",        # Харизма
        }

        # Получаем атрибут, связанный с этим навыком
        attribute = skill_attributes.get(skill)

        # Если навыка нет в словаре, возвращаем 0
        if not attribute:
            print(f"Навыка '{skill}' не существует!")
            return 0

        # Определяем бонус по атрибуту
        attribute_bonus = (getattr(self, attribute) - 10) // 2

        # Если персонаж обучен этому навыку (значение True), добавляем бонус
        base_skill_bonus = 0
        if self.skills.get(skill, False):  # Проверяем, обучен ли навык
            base_skill_bonus = 2  # Обычно это +2 за обучение

        return base_skill_bonus + attribute_bonus
    
    def add_experience(self, xp: int) -> None:
        """Добавление опыта и повышение уровня, если достигнут порог."""
        self.experience += xp
        # Таблица опыта для достижения уровней (D&D 5e)
        level_thresholds = [
            0,      # 1 уровень: 0 опыта
            300,    # 2 уровень: 300 опыта
            900,    # 3 уровень: 900 опыта
            2700,   # 4 уровень: 2700 опыта
            6500,   # 5 уровень: 6500 опыта
            14000,  # 6 уровень: 14000 опыта
            23000,  # 7 уровень: 23000 опыта
            34000,  # 8 уровень: 34000 опыта
            48000,  # 9 уровень: 48000 опыта
            64000,  # 10 уровень: 64000 опыта
            85000,  # 11 уровень: 85000 опыта
            100000, # 12 уровень: 100000 опыта
            120000, # 13 уровень: 120000 опыта
            140000, # 14 уровень: 140000 опыта
            165000, # 15 уровень: 165000 опыта
            195000, # 16 уровень: 195000 опыта
            225000, # 17 уровень: 225000 опыта
            265000, # 18 уровень: 265000 опыта
            305000, # 19 уровень: 305000 опыта
            355000  # 20 уровень: 355000 опыта
        ]
        
        # Проверяем, достиг ли персонаж порога опыта для повышения уровня
        while self.level < 20 and self.experience >= level_thresholds[self.level]:
            self.level_up()

    def level_up(self) -> None:
        """Повышение уровня и пересчет здоровья."""
        self.level += 1
        print(f"{self.name} повысил уровень до {self.level}!")
        self.hp = self.calculate_hp()  # Пересчитываем здоровье при повышении уровня

    def is_alive(self) -> bool:
        """Проверка, жив ли персонаж."""
        if self.hp > 0:
            return True
        print(f"{self.name} погиб!")
        return False
    
    def take_damage(self, damage: int):
        """Персонаж получает урон и теряет здоровье."""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} получает {damage} урона, текущее здоровье: {self.hp}")

    def heal(self, amount: int):
        """Лечение персонажа, восстановление здоровья."""
        self.hp += amount
        print(f"{self.name} восстанавливает {amount} здоровья, текущее здоровье: {self.hp}")



    def add_item(self, item: str):
        """Добавление предмета в инвентарь."""
        self.inventory.append(item)
        print(f"{self.name} добавляет {item} в инвентарь.")

    def remove_item(self, item: str):
        """Удаление предмета из инвентаря."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{self.name} удаляет {item} из инвентаря.")
        else:
            print(f"{self.name} не имеет {item} в инвентаре.")


    def cast_spell(self, spell: str) -> None:
        """Магия: проверка, есть ли заклинание в списке и каст."""
        if spell in self.spells:
            print(f"{self.name} использует заклинание {spell}.")
        else:
            print(f"{self.name} не знает заклинания {spell}.")

    def learn_skill(self, skill: str, level: int = 1):
        self.skills[skill] = level

    def learn_spell(self, spell: str):
        """Изучение нового заклинания."""
        if spell not in self.spells:
            self.spells.append(spell)
            print(f"{self.name} изучает заклинание {spell}.")
        else:
            print(f"{self.name} уже знает заклинание {spell}.")


    def show_stats(self) -> None:
        """Вывод характеристик персонажа."""
        print(f"Персонаж: {self.name}")
        print(f"Раса: {self.race}, Класс: {self.char_class}")
        print(f"Уровень: {self.level}, Опыт: {self.experience}")
        print(f"Сила: {self.strength}, Ловкость: {self.dexterity}, Телосложение: {self.constitution}")
        print(f"Интеллект: {self.intelligence}, Мудрость: {self.wisdom}, Харизма: {self.charisma}")
        print(f"Здоровье: {self.hp}")
        print(f"Инвентарь: {self.inventory}")
        print(f"Навыки: {self.skills}")
        print(f"Заклинания: {self.spells}")
    
    def get_experience(self) -> int:
        """Возвращает текущий опыт"""
        return self.experience


    def __repr__(self):
        return f"<{self.char_class} {self.name} (Lvl {self.level}, HP {self.hp},)>"



# Пример создания персонажа:
character = Character(
    name="Грог",
    race="Человек",
    char_class="Воин",
    level=1,
    strength=16,
    dexterity=14,
    constitution=14,
    intelligence=10,
    wisdom=8,
    charisma=12,
    experience=0,
    inventory=["Меч", "Щит"],
    skills={
        "Акробатика": True,  # Обучен
        "Атлетика": False,   # Не обучен
        "Магия": False,      # Не обучен
        "Скрытность": True,  # Обучен
        "Выступление": True, # Обучен
    },
    spells=[],  # Воин не использует магию по умолчанию
)

# Пример работы:
character.show_stats()
# print(character.hp)
# print(character.experience)

# character.add_experience(305000)  # Добавление опыта, повышение уровня
# character.cast_spell("Огненный шар")  # Попытка применить заклинание

# print(character.hp)
# print(character.experience)

# print(character.calculate_skill_bonus('Атлетика'))
