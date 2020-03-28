def input_data(string):
    poll_data = string.split(" ")
    a = 0
    b = 0
    while True:
        try:
            # ввод знака
            s = poll_data[0]
            assert(s in ('+','-','*','/')), "Неверный знак операции!"
            #ввод положительного 1 числа

            x = int(poll_data[1])
            y = int(poll_data[2])

            if x < 0:
                print("Внимание, вы ввели не положительное первое число!")
                x = int(input('первое число = '))

            if y < 0:
                print("Внимание, вы ввели не положительное второе число!")
                y = int(input('второе число = '))


            if s == '+':
                print('Результат:', x + y)
                break
            elif s == '-':
                print('Результат:', x - y)
                break
            elif s == '*':
                print('Результат:', x * y)
                break
            elif s == '/':
                try:
                    print('Результат:', x / y)
                    break
                except ZeroDivisionError:
                    print("На ноль делить нельзя!")
                    break
        #вывод уведомление о неправильном введеном знаке
        except AssertionError as msg:
            print(msg)

string = input("введите данные в следующем формате через пробел: + 2 2 \n")
input_data(string)




# while True:
#     try:
#         # ввод знака
#         s = input("Знак (+,-,*,/): ")
#         assert(s in ('+','-','*','/')), "Неверный знак операции!"
#
#         a = 0
#         b = 0
#
#         #ввод положительного 1 числа
#         while a != 1:
#             try:
#                 x = int(input("х="))
#             except ValueError:
#                 print("Пожалуйста, введите положительное число")
#             else:
#                 if x < 0:
#                     print("Вы ввели не положительное число, повторите ввод")
#                 else:
#                     a = a + 1
#
#         # ввод положительного 2 числа
#         while b != 1:
#             try:
#                 y = int(input("y="))
#             except ValueError:
#                 print("Пожалуйста, введите положительное число")
#             else:
#                 if y < 0:
#                     print("Вы ввели не положительное число, повторите ввод")
#                 else:
#                     b = b + 1
#
#         if s == '+':
#             print(x + y)
#         elif s == '-':
#             print(x - y)
#         elif s == '*':
#             print(x * y)
#         elif s == '/':
#             try:
#                 print(x / y)
#             except ZeroDivisionError:
#                 print("На ноль делить нельзя")
#
#     #вывод уведомление о неправильном введеном знаке
#     except AssertionError as msg:
#         print(msg)
