HELP = '''
help - вывести на экран, что умеет бот.
add - добавить задачу в список (запрашиваем у пользователя).
show - напечатать все добавленные задачи.'''

tasks = {

}

# Сегодня, завтра, 31.12 ...
# [Задача 1, Задача2, Задача3]
# Дата -> [Задача 1, Задача2, Задача3]

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
           for task in tasks[date]:
               print('_ ', task)
           else:
               print("Такой даты нет!")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи:\n")
        if date in tasks:
            # Дата есть в словаре
            # Добавляем в список задачу
            tasks[date].append(task)
        else:
            # Даты в словаре нет
            # Создаем запись с ключом date
            tasks[date] = []
            tasks[date].append(task)
        print("Задача", tasks, "добавлена на дату", date)
    else:
     print("Неизвестная команда!")
     break
