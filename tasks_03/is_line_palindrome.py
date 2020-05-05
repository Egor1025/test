def func(text):
    text_update_1 = text.replace(' ', '')
    text_update_2 = list(text_update_1)
    text_update_2.reverse()
    if text_update_2 == list(text_update_1):
        answer = 'да, эта строка палиндром'
    else:
        answer = 'нет, это строка не палиндромххххххх'
    return answer


print(func(input('введите текст: ')))
