# Завдання 1
# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.
from collections import deque
import time

class ServerQueue:
    def __init__(self):
        self.client_queue = deque()
        self.request_stats = deque()

    def add_client(self, client_name, priority):
        self.client_queue.append((client_name, priority))
        self.client_queue = deque(sorted(self.client_queue, key=lambda x: x[1], reverse=True))

    def process_request(self):
        if self.client_queue:
            client, _ = self.client_queue.popleft()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.request_stats.append((client, timestamp))
            print(f"Оброблено запит від клієнта {client} о {timestamp}")
        else:
            print("Черга запитів порожня")

    def show_stats(self):
        print("Статистика запитів:")
        for client, timestamp in self.request_stats:
            print(f"Клієнт: {client}, Час запиту: {timestamp}")

def display_menu():
    print("Меню:")
    print("1. Додати нового клієнта")
    print("2. Обробити наступний запит")
    print("3. Показати статистику запитів")
    print("0. Вихід")

server = ServerQueue()

while True:
    display_menu()
    choice = input("Оберіть операцію: ")

    if choice == '1':
        client_name = input("Введіть ім'я клієнта: ")
        priority = int(input("Введіть пріоритет клієнта (чим більше число, тим вищий пріоритет): "))
        server.add_client(client_name, priority)
    elif choice == '2':
        server.process_request()
    elif choice == '3':
        server.show_stats()
    elif choice == '0':
        print("Дякую за користування! Завершення програми.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
