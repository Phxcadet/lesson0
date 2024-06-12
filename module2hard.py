chislo = int(input('Введите число: '))
spis = []
for i in range(1, chislo):
    spis.append(i)
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
