# TODO Запишите функцию `factorial`
def factorial(n, g = 1):
    if type(n) == int:
        if n == 0:
            g = 1
        else:
            for i in range(1, n+1):
                g = g*i
    return g
f_0 = factorial(0)
f_5 = factorial(5)

# TODO Вызовите функцию factorial и распечатайте результат 
print(f"Факториал числа 0 равен {f_0}")
print(f"Факториал числа 5 равен {f_5}")
