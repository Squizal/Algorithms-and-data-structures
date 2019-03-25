print("Введите 0 (ноль) чтобы выйти из калькулятора")
#Используем бесконечный цикл с выходом через 0 (ноль)
while True:
        operation = input("Выберите операцию: +, -, *, / ")
        if operation == '0': break
        if operation in ('+','-','*','/'):
#Добавляем возможность использования чисел с плавающей точкой
                a = float(input("a="))
                b = float(input("b="))
                if operation == '+':
#Округляем до 2-х знаков после запятой и подставляем значения через %
                        print("%.2f" % (a+b))
                elif operation == '-':
                        print("%.2f" % (a-b))
                elif operation == '*':
                        print("%.2f" % (a*b))
                elif operation == '/':
                        if b != 0:
                                print("%.2f" % (a/b))
                        else:
                                print("На ноль делить нельзя!")
        else:
                print("Выберите верный знак!")