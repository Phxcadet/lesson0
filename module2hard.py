# chislo = int(input('Введите число: '))
# spis = []
# for i in range(1, chislo):
#     spis.append(i)
# print('Числа друг за другом: ' , spis)
# finish = len(spis)
# print('Последнее число в списке: ', finish)
# for i in range(1, finish):
#     print(spis[i-1] + spis[i])
# _____
# list_2 = []
# if (spis[0] + spis[1]) % chislo == 0:
#     list_2.append(spis[0])
#     list_2.append(spis[1])
# print(list_2)
# ______
chislo = int(input('Введите число: '))
spis = []
for i in range(1, chislo):
    spis.append(i)
# print('Числа друг за другом: ' , spis)
# print('Последнее число в списке: ', finish)
result = []
for i in spis:
    for j in spis:
        if i == j:
            continue
        if i < j:
            s = i+j
            if chislo % s == 0:
                result.append(i)
                result.append(j)
print(result)
