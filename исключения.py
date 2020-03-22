while True:
    try:
        # ввод знака
        s = input("Знак (+,-,*,/): ")
        assert(s in ('+','-','*','/')), "Неверный знак операции!"

        a = 0
        b = 0

        #ввод положительного 1 числа
        while a != 1:
            try:
                x = int(input("х="))
            except ValueError:
                print("Пожалуйста, введите положительное число")
            else:
                if x < 0:
                    print("Вы ввели не положительное число, повторите ввод")
                else:
                    a = a + 1

        # ввод положительного 2 числа
        while b != 1:
            try:
                y = int(input("y="))
            except ValueError:
                print("Пожалуйста, введите положительное число")
            else:
                if y < 0:
                    print("Вы ввели не положительное число, повторите ввод")
                else:
                    b = b + 1

        if s == '+':
            print(x + y)
        elif s == '-':
            print(x - y)
        elif s == '*':
            print(x * y)
        elif s == '/':
            try:
                print(x / y)
            except ZeroDivisionError:
                print("На ноль делить нельзя")

    #вывод уведомление о неправильном введеном знаке
    except AssertionError as msg:
        print(msg)