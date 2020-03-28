from datetime import datetime
import time

start_time = time.time()
a = 0

with open('manager_logs.csv', 'a', encoding="utf8") as opened_file:
    opened_file.write(f'\n\nВремя запуска кода в менеджере контекста: {datetime.now()}')
    for i in range(10000):
        a = a + i
    opened_file.write(f'\nРезультат программы a = {a}')
    opened_file.write(f'\nВремя окончания работы кода: {datetime.now()}')
    spend_time = time.time() - start_time
    opened_file.write(f'\nСколько было потрачено времени на выполнение кода: {spend_time} секунд')
