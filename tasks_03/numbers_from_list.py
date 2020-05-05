def func(text):
    nums = []
    list = text.split(' ')
    for i in list:
        if i.isdigit():
            nums.append(i)
    return nums


print(func(input('введите текст: ')))