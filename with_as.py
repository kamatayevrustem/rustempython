from contextlib import contextmanager
from datetime import datetime
import time
start_time = time.time()
a = 0

@contextmanager
def open_file(name):
    f = open(name, 'w')

    yield f
    print(f'Время запуска кода в менеджере контекста: {datetime.now()}')
    print(f'Результат программы a = {a}')
    print(f'Время окончания работы кода: {datetime.now()}')
    spend_time = time.time() - start_time
    print(f'Сколько было потрачено времени на выполнение кода: {spend_time} секунд \n\n')
    f.close()

with open_file('some_fil2e.txt') as f:
    f.write('hola!')
