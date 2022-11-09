HELP = '''
help - вывести на экран, что умеет бот.
add - добавить задачу в список (запрашиваем у пользователя).
show - напечатать все добавленные задачи.'''

tasks = {


}

#Сегодня, завтра, 31.12 ...
#[Задача 1, Задача2, Задача3]
#Дата -> [Задача 1, Задача2, Задача3]

run = True

while run:
    command = input("Введите команду\n")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        date = input("Введите дату для добавления задачи")
        tasks = input("Введите название задачи:\n ")
        tasks.append(task)