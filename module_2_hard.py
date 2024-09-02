n = int(input('Введите число от 3 до 20: '))

while n > 20 or n < 3:
    n = int(input('Вы ввели число не в диапозоне от 3 до 20, попробуйте ещё раз:' ))

yes_no = 0
pair = []
list_1 = []

for i in range(n+1):
    if i == 0:
        continue
    for j in range(n+1):
        if i == 0 or j == 0:
            continue
        elif n % (j+i) == 0:
            yes_no = 1
            list_1.append([j, i])
        else:
            yes_no != 1
            yes_no = 0
        if [i, j] not in pair and yes_no == 1:
            pair.append([j, i])

print('Пары',*pair)
password = sum(pair, [])
print('Код', *password)




