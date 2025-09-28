import random
from typing import Dict, List, Optional


class Monster:
    def __init__(
        self,
        name: str,
        monster_type: str,
        size: str,
        armor_class: int,
        hit_dice: str,
        speed: str,
        strength: int,
        dexterity: int,
        constitution: int,
        intelligence: int,
        wisdom: int,
        charisma: int,
        challenge: float,
        xp: int,
        skills: Optional[Dict[str, int]] = None,
        senses: Optional[List[str]] = None,
        languages: Optional[List[str]] = None,
        resistances: Optional[List[str]] = None,
        actions: Optional[Dict[str, str]] = None,
        loot: Optional[List[str]] = None,
        vulnerabilities: Optional[List[str]] = None,   # 🔹 уязвимости
        immunities: Optional[List[str]] = None,        # 🔹 иммунитеты
    ):
        self.name = name
        self.monster_type = monster_type
        self.size = size
        self.armor_class = armor_class
        self.hit_dice = hit_dice
        self.hp = self.roll_hp(hit_dice)
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.challenge = challenge
        self.xp = xp
        self.skills = skills or {}
        self.senses = senses or []
        self.languages = languages or []
        self.resistances = resistances or []
        self.actions = actions or {}
        self.loot = loot or []
        self.vulnerabilities = vulnerabilities or []
        self.immunities = immunities or []

    def roll_hp(self, dice_expr: str) -> int:
        """Бросает кубики для хитов монстра (например 2d6+2)."""
        try:
            parts = dice_expr.lower().replace(" ", "")
            base, *mod = parts.split("+")
            num, sides = map(int, base.split("d"))
            hp = sum(random.randint(1, sides) for _ in range(num))
            if mod:
                hp += int(mod[0])
            return hp
        except Exception:
            return 1

    def attack(self, action_name: str) -> None:
        if action_name in self.actions:
            print(f"{self.name} использует {action_name}: {self.actions[action_name]}")
        else:
            print(f"{self.name} не имеет действия '{action_name}'.")

    def drop_loot(self) -> List[str]:
        """Возвращает случайный лут из списка."""
        if not self.loot:
            return []
        drop = random.sample(self.loot, k=random.randint(1, min(2, len(self.loot))))
        print(f"{self.name} дропнул: {drop}")
        return drop

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} получает {damage} урона, текущее здоровье: {self.hp}")

    def show_stats(self):
        print(f"Монстр: {self.name} ({self.size} {self.monster_type})")
        print(f"Класс брони: {self.armor_class}, Хиты: {self.hp} ({self.hit_dice}), Скорость: {self.speed}")
        print(f"Сила: {self.strength}, Ловкость: {self.dexterity}, Телосложение: {self.constitution}")
        print(f"Интеллект: {self.intelligence}, Мудрость: {self.wisdom}, Харизма: {self.charisma}")
        print(f"Опасность (CR): {self.challenge}, Опыт: {self.xp}")
        print(f"Навыки: {self.skills}, Чувства: {self.senses}, Языки: {self.languages}")
        print(f"Сопротивления: {self.resistances}")
        print(f"Атаки/Умения: {list(self.actions.keys())}")
        print(f"Лут: {self.loot}")
        print(f"Сопротивления: {self.resistances}, Уязвимости: {self.vulnerabilities}, Иммунитеты: {self.immunities}")


    def __repr__(self):
        return f"<Монстр {self.name} (CR {self.challenge}, HP {self.hp})>"
    
    BASE_HP = {
        "Гоблин": 7,           # обычно 2d6 ~ 7
        "Орк": 15,             # 2d8+6 ~ 15
        "Скелет": 13,          # 2d8+4 ~ 13
        "Бандит": 11,          # 2d8+2 ~ 11
        "Тролль": 84,          # 8d10+40 ~ 84
        "Огненный элементаль": 114,  # 12d10+24 ~ 114
        "Молодой зелёный дракон": 136, # 16d10+48 ~ 136
        "Волк": 11,            # 2d8+2
        "Паук": 7,             # 2d4+2
        "Зомби": 22            # 3d8+9
    }

    def calculate_hp(self) -> int:
        """Вычисление HP по типу монстра и конституции"""
        base = self.BASE_HP.get(self.name, 10)
        con_mod = (self.constitution - 10) // 2
        hp = base + con_mod

        # Если уровень > 1, добавляем здоровье за каждый уровень (по кубику base)
        for _ in range(1, self.level):
            hp += random.randint(1, base) + con_mod
        return hp



# ====== Примеры монстров ======
goblin = Monster(
    name="Гоблин",
    monster_type="гуманоид",
    size="Малый",
    armor_class=15,
    hit_dice="2d6",
    speed="9 м.",
    strength=8,
    dexterity=14,
    constitution=10,
    intelligence=10,
    wisdom=8,
    charisma=8,
    challenge=0.25,
    xp=50,
    skills={"Скрытность": 6},
    senses=["Тёмное зрение 18 м."],
    languages=["Общий", "Гоблинский"],
    actions={"Сабля": "+4 к атаке, 1d6+2 рубящий", "Короткий лук": "+4 к атаке, 1d6+2 колющий"},
    loot=["Ржавый кинжал", "Кусок кожи", "5 монет меди"],
    vulnerabilities=["огонь"],
    immunities=["яд"] 
)


goblin.show_stats()
goblin.drop_loot() 