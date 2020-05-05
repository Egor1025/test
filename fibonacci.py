
x = 1  # вторая единица в ряду чисел 1,1,2,3,5...
y = 1  # первая единица
n = int(input('введите позицию числа Фибоначчи: '))


def fib(n, x, y):
    if n == 1:
        return y
    else:
        x += y
        y = x - y
        return fib(n - 1, x, y)


print(fib(n, x, y))