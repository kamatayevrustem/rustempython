from datetime import datetime
import time

start_time = time.time()
a = 0

with open('manager_logs.csv', 'a', encoding="utf8") as opened_file:
    opened_file.write(f'Время запуска кода в менеджере контекста: {datetime.now()}')

    # переменные
    age = int(input('Сколько вам лет ', ))  # вопрос для проверки на годность
    if age >= 18:
        study_now = input('Вы сейчас учитесь? введите да/нет ', )  # вопрос для справки
        height = int(input('Какой у вас рост ', ))  # вопрос для справки
        count_of_children = int(input('Сколько у вас детей ', ))  # вопрос для проверки на годность
        if count_of_children == 0:
            if height < 170:
                print('В танкисты')
            elif height < 185:
                print('Во флот')
            elif height < 200:
                print('В десантники')
            elif height >= 200:
                print('В ФСБ')
        else:
            print('Вы негодны, потому что у вас есть дети')
    else:
        print('Вы негодны, потому что вам нет 18 лет')

    opened_file.write(f'\nРезультат программы a = {a}')
    opened_file.write(f'\nВремя окончания работы кода: {datetime.now()}')
    spend_time = time.time() - start_time
    opened_file.write(f'\nСколько было потрачено времени на выполнение кода: {spend_time} секунд \n\n')
