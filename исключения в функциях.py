# функции
documents = [
        {"type": "passport", "number": "12345", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006"}
      ]

documents2 = [
        {"type": "passport", "number": "12345", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': ['12345']
      }

#Задача №3
# Расширить домашние задание из лекции 2.1
# «Функции — использование встроенных и создание собственных» новой функцией,
# выводящей имена всех владельцев документов.
# помощью исключения KeyError проверяйте, есть ли поле "name" у документа.
# Сделал новый поиск / update добавил проверку KeyError
def show_document_new(list):
    """просто выводим по формату значения"""
    print('У меня в базе есть эти документы')
    for i in documents:
        try:
            print('passport ' '"' "№ {}" '"' ' "' "{}" '"'.format(i['number'],i['name']))
        except KeyError:
            print('passport' '" ' "№ {}" '" - отсутствует поле name!'.format(i['number']))

#старый поиск и остальные функции я не трогал, но смысл try/except прекрасно понял, спасибо вам!
def show_document(list):
    """просто выводим по формату значения"""
    print('У меня в базе есть эти документы')
    for i in documents:
        print('passport ' '"' "{}" '"' ' "' "{}" '"'.format(i['number'],i['name']))

def find_people(list):
    """вводим номер документа и выводим имя человека"""
    number_name = input('Введние номер документа: ')
    for i in documents:
        if i['number'] == number_name:
            name = i['name']
            print(name)
            return name
    else: print('Документ не найден')

# def delete_document(list):
#     """вводим номер документа и выводим имя человека"""
#     number_name = input('Введние номер документа: ')
#     for i in documents:
#         if i['number'] == number_name:
#             documents[i].remove
#     print(documents)
#
#     for i in documents:
#         if i['number'] == number_name:
#             name = i['name']
#             print(name)
#     return name




def find_shelf(dict):
    """просто выводим по формату значения"""
    temp = 0
    number_name = input('Введите номер документа: ')
    for key, value in directories.items():
        if number_name in value:
            print('Документ с номером', number_name, 'лежит на полке №', key)
        # else:
        #     print('Документ с номером не лежит на полке под номером', key )
        if number_name not in value:
            print('Документ с номером', number_name, 'не лежит на полке №', key)

def add_data(list,dict):
    """добавляем данные в список"""
    count_shelf = len(directories)
    count_shelfadd = count_shelf+1
    type = input('Введние тип документа: ')
    number = input('Введние номер документа: ')
    name = input('Введние имя владельца: ')
    print('Спасибо! Ваш документ будет добавлен на полку: ', count_shelfadd)
    documents.append({'type': type, 'number': number, 'name': name})

    directories.update({count_shelfadd : [number]})  #первый метод добавления
    directories[count_shelfadd+1] = [number] #второй метод добавления -


    print(documents)
    print(directories)

def commands(command):
    if command == '1':
        show_document_new(documents)
    elif command == '2':
        find_people(documents)
    elif command == '3':
        find_shelf(directories)
    elif command == '4':
        add_data(documents, directories)
    elif command == '5':
        print('До свидания, рада была вам помочь!')
        global a
        a = 1

#вызов функции
# find_people(documents)
# show_document(documents)
# find_shelf(directories)
# add_data(documents,directories)

print('Вас приветствует онлайн-секретарь Диана!')
print('Я умею выполнять команды:\n'
      '1. могу показать все документы \n'
      '2. найти имя при вводе номера документа \n'
      '3. искать номер полки на которой лежит документ \n'
      '4. могу добавить документ \n'
      '5. выйти из программы \n')
a = 0
while a==0:
    command = input('\nВведите номер команды: ')
    commands(command)
    if a == 0:
        answer = input('\nВы ходите выполнить еще одну команду? \nВведите да или нет: ')
        if answer == 'да':
            continue
        else:
            print('До свидания, рада была вам помочь!')
            break
documents.append({'type': 1, 'number': 2, 'name': 3})

