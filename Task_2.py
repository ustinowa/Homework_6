
# Task_4
# Сжатие данных
def func(string):

    new_string = ''
    count = 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            new_string += str(count) + string[i]
            count = 1
        else:
            count += 1

        if i == len(string) - 2:
            new_string += str(count) + string[i]

    return new_string

print(func('FFFFBBBHHHYYYYAAVFFFFF'))


### Восстановление данных
def func_1(string1):

    new_string1 = ''
    new_string1 = [string1[i+1] * int(string1[i]) for i in range(len(string1) - 1) if string1[i].isdigit()]

    return new_string1

print(func_1('4F3B3H4Y2A1V4F'))
