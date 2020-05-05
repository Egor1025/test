def find_roots(equation):
    equation = list(equation)
    a = []
    b = []
    c = []
    for i in equation:
        if i.isdigit():
            a.append(i)
        elif i == '-':
            a.append(i)
        else:
            equation.remove(i)
            break
    for i in a:
        equation.remove(i)
    equation.remove('2')
    a = ''.join(a)
    for i in equation:
        if i.isdigit():
            b.append(i)
        elif i == '-':
            b.append(i)
        elif i.isalpha():
            equation.remove(i)
            break
    for i in b:
        equation.remove(i)
    b = ''.join(b)
    for i in equation:
        if i.isdigit():
            c.append(i)
        elif i == '-':
            c.append(i)
        elif i == '=':
            break
    c = ''.join(c)
    D = int(b) ** 2 - 4 * int(a) * int(c)
    if int(D) < 0:
        return 'корней нет'
    elif D == 0:
        x = (-int(b)) / (2 * int(a))
        return x
    else:
        x1 = (-int(b) + int(D) ** (1 / 2)) / (2 * int(a))
        x2 = (-int(b) - int(D) ** (1 / 2)) / (2 * int(a))
        return x1, x2


print(find_roots(input('введите кв. уравнение в стандртном виде: ')))