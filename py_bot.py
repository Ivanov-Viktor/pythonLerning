HELP = """
help - Напечатать справку по программе.
add - Добавить задачу в список (название задачи запрашиваем у пользователя).
show - Напечатать все добавленные задачи"""

tasks = []

run = True

while run:
    command = input("Ведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        print("Задача добавлена!")
    else:
        print("Неизвестная команда")
        break

print("До свидания!")