todos: dict = dict()  # todos = {}
todos: list = list()  # todos = []

HELP = '''
Список доступных команд:
* print/show  - напечать все задачи на заданную дату
* todo - добавить задачу
* help - Напечатать help
'''

stop = False
while not stop:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'todo':
        task = input('Введите задачу: ')
        todos.append(task)
        # Альтернативный вариант:
        # print('Задача ' + task + ' добавлена')
        print(f'Задача {task} добавлена')
    elif (command == 'print') or (command == 'show'):
        print(todos)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        stop = True
    else:
        print('Неизвестная команда!')
        print(HELP)
        stop = True
