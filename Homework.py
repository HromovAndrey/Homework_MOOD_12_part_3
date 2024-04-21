# Завдання 2
# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний
# час доби;
# 2. Середній час між появою катерів на причалі у різний час
# доби;
# 3. Тип зупинки катера (кінцева або інша).
# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно

import random
import time

class Passenger:
    def __init__(self):
        self.stay_time = random.uniform(5, 15)
class Boat:
    def __init__(self, capacity):
        self.capacity = capacity

class Dock:
    def __init__(self):
        self.passenger_arrival_time = random.uniform(5, 20)
        self.boat_arrival_time = random.uniform(30, 60)
        self.boat_stop_type = random.choice(["кінцева", "інша"])
        self.passengers = []
        self.boats = []

    def add_passenger(self):
        self.passengers.append(Passenger())

    def add_boat(self, capacity):
        self.boats.append(Boat(capacity))

    def process(self):
        if random.random() < 0.5:
            self.add_passenger()

        if random.random() < 0.2:
            capacity = random.randint(5, 20)
            self.add_boat(capacity)

        for passenger in self.passengers:
            if random.random() < 0.1:
                if self.boats:
                    boat = self.boats.pop(0)
                    boat_capacity = min(boat.capacity, len(self.passengers))
                    for _ in range(boat_capacity):
                        self.passengers.pop(0)
                    print(f"Катер відправився з {boat_capacity} пасажирами о {time.strftime('%H:%M:%S')}")

        time.sleep(1)

dock = Dock()

for _ in range(100):
    dock.process()

