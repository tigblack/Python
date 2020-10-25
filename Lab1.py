import sys
from math import sqrt

print("ИУ5-52Б Саргсян Тигран Артурович")
print("Введите коэффициенты a, b и c")

def solver(a, b, c):
    if a == 0:
        var1 = -c/b
        if var1 < 0:
            print("Нет корней")
        elif var1 == 0:
            print("x1 = 0")
        else:
            x1 = sqrt(var1)
            x2 = -sqrt(var1)
            print('x1 = {}, x2 = {}'.format(x1, x2))
            sys.exit()

    if b == 0:
        var2 = -c/a
        if var2 < 0:
            print("Нет корней")
        elif var2 == 0:
            print("x1 = 0")
        else:
            y1 = sqrt(var2)
            x1 = sqrt(y1)
            x2 = -sqrt(y1)
            print("x1 = {}, x2 = {}".format(x1, x2))
            sys.exit()
    else:
        D = pow(b, 2) - (4 * a * c)
        if D < 0:
            print("Нет корней")
        else:
            y1 = ((-b - sqrt(D)) / (2 * a))
            y2 = ((-b + sqrt(D)) / (2 * a))
            if y1 > 0 and y2 > 0:
                x1 = sqrt(y1)
                x2 = -sqrt(y1)
                x3 = sqrt(y2)
                x4 = -sqrt(y2)
                print("x1 = {}, x2 = {}, x3 = {}, x4 = {}".format(x1, x2, x3, x4))


text = "Коэффициент введён неправильно, попробуйте снова"
if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except:
        print("Неправильно введены коэффициенты")
        exit()
else:
    while 1:
        try:
            a = float(input())
            break
        except:
            print(text)
    while 1:
        try:
            b = float(input())
            break
        except:
            print(text)
    while 1:
        try:
            c = float(input())
            break
        except:
            print(text)
if a == 0 and b == 0 and c == 0:
    print("Бесконечное число корней")
elif a == 0 and b == 0:
    print("Корней нет")
else:
    solver(a,b,c)
