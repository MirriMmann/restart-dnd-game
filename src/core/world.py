# src\core\world.py

from src.core.character import Character
import random
import time

class TimeOfDay:
    """Класс для определения времени суток и других факторов."""
    def __init__(self):
        self.hours = 6  # Часы (0 - 23)
        self.minutes = 0  # Минуты (0 - 59)
        self.day = 1  # День (1 - n)
        self.season = "Spring"  # Сезон (Весна, Лето, Осень, Зима)
        self.weather = "Clear"  # Погода (Ясно, Дождь, Снег и т.д.)
        self.day_cycle = ["Morning", "Afternoon", "Evening", "Night"]  # Цикл дня и ночи
        self.weather_conditions = ["Clear", "Rain", "Snow", "Thunderstorm", "Fog", "Windy"]

    def increment_time(self, days=0, hours=0, minutes=0):
        """Увеличивает время на заданное количество дней, часов и минут, корректно обрабатывая переносы."""
        self.minutes += minutes
        extra_hours_from_minutes = self.minutes // 60
        self.minutes %= 60

        self.hours += hours + extra_hours_from_minutes
        extra_days_from_hours = self.hours // 24
        self.hours %= 24

        self.day += days + extra_days_from_hours
        self.update_season()

    def update_time(self):
        """Обновление времени."""
        self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1
        if self.hours >= 24:
            self.hours = 0
            self.day += 1
            self.update_season()

    def update_season(self):
        """Обновление сезона в зависимости от дня в году."""
        days_in_year = 365
        day_of_year = self.day % days_in_year
        # Учитываем сезон в зависимости от дня в году
        if day_of_year <= (days_in_year // 4):
            self.season = "Spring"
        elif day_of_year <= (days_in_year // 2):
            self.season = "Summer"
        elif day_of_year <= (days_in_year * 3 // 4):
            self.season = "Fall"
        else:
            self.season = "Winter"

    def get_time_of_day(self):
        """Определить текущее время суток (Утро, День, Вечер, Ночь)."""
        if 6 <= self.hours < 12:
            return self.day_cycle[0]  # Утро
        elif 12 <= self.hours < 18:
            return self.day_cycle[1]  # День
        elif 18 <= self.hours < 21:
            return self.day_cycle[2]  # Вечер
        else:
            return self.day_cycle[3]  # Ночь

    def change_weather(self):
        """Определить погоду (динамично меняется)."""
        return random.choice(self.weather_conditions)

    def next_day(self):
        """Переводит время в следующий день."""
        self.day += 1
        self.hours = 6
        self.minutes = 0
        self.weather = self.change_weather()  # Обновляем погоду
        self.update_season()

    def get_formatted_time(self):
        """Отображение времени в формате: Часы:Минуты"""
        return f"{self.hours:02}:{self.minutes:02}"
    
    def check_daily_event(self):
        """Проверяет, нужно ли провести событие на основе текущего времени суток."""
        if self.get_time_of_day() == "Morning":
            self.trigger_event("Morning Quest")
        if self.get_time_of_day() == "Night":
            self.trigger_event("Night Patrol")
        if self.weather == "Rain":
            self.trigger_event("Rain Event")

    def trigger_event(self, event_name):
        """Запускает событие."""
        print(f"Event triggered: {event_name}")
    
    def __repr__(self):
        return f"Day: {self.day} Time: {self.get_formatted_time()} ({self.get_time_of_day()}), Season: {self.season}, Weather: {self.weather}"

class World:
    """Класс мира, включающий в себя элементы времени, погоды, сезонности и событий."""
    def __init__(self, name, setting):
        self.name = name
        self.setting = setting  # Тематика мира (фэнтези, постапокалипсис, и т.д.)
        self.regions = []  # Список регионов
        self.entities = []  # Существа и объекты мира
        self.events = []  # События, зависящие от времени и погоды
        self.time = TimeOfDay()

    def add_region(self, region):
        """Добавить регион в мир."""
        self.regions.append(region)

    def add_entity(self, entity):
        """Добавить существо или объект в мир."""
        self.entities.append(entity)

    def add_event(self, event):
        """Добавить событие, зависящее от времени и погоды."""
        self.events.append(event)

    def update_world(self):
        """Обновить мир: увеличиваем время, проверяем события."""
        self.time.update_time()
        self.trigger_time_based_events()

    def trigger_time_based_events(self):
        """Запуск событий, которые зависят от времени суток, сезона или погоды."""
        if self.time.get_time_of_day() == "Night":
            self.night_events()
        elif self.time.get_time_of_day() == "Morning":
            self.morning_events()

        if self.time.weather == "Rain":
            self.weather_events("Rain")

    def night_events(self):
        """События, происходящие ночью."""
        print("Nighttime events triggered...")

    def morning_events(self):
        """События, происходящие утром."""
        print("Morning events triggered...")

    def weather_events(self, weather_type):
        """События, зависящие от погоды."""
        print(f"Weather event triggered: {weather_type}")

    def __repr__(self):
        return f"World(name={self.name}, setting={self.setting}, {len(self.entities)} entities, time={self.time})"



# Создание мира
world = World(name="Epsilon", setting="Modern Post-Apocalypse")


# Добавление сущностей (например, NPC или локаций)
world.add_entity(
    Character(
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
)
world.add_entity(
    Character(
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
)

print(world)
# print(world.entities)

# Запуск мира и событий
# for _ in range(4):  # Симуляция суток (24 часа)
#     world.update_world()
#     print(world.time)  # Отображение текущего времени и погоды
#     time.sleep(1)  # Задержка в 1 секунду для имитации времени


