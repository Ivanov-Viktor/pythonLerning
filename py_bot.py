# HELP = """
# help - Напечатать справку по программе.
# add - Добавить задачу в список (название задачи запрашиваем у пользователя).
# show - Напечатать все добавленные задачи
# delete - Удалить задачу
# exit - Выйти из бота"""
#
# tasks = []
#
# run = True
#
# while run:
#     command = input("Ведите команду: ")
#     if command == "help":
#         print(HELP)
#     elif command == "show":
#         print(tasks)
#     elif command == "add":
#         task = input("Введите название задачи: ")
#         tasks.append(task)
#         print("Задача добавлена!")
#     else:
#         print("Неизвестная команда")
#         break
#
# print("До свидания!")


HELP = """
help - напечатать строку о программе
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - показать все добавленные задачи
print - вывести на экран
exit - выход. """

today = []
tomorrow = []
other = []

while True:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        date = input("Введите дату выполнения задачи: ")
        task = input("Введите название задачи: ")
    if date == "Сегодня":
        today.append(task)
    elif date == "Завтра":
        tomorrow.append(task)
    else:
        other.append(task)
    elif command == 'print':
        print(today, tomorrow, other)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
    else:
         print("Неизвестная задача")
            break
    print("До свидания")

    print("Неизвестная команда - ", command)
            break
