grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
A = (grades[0][0] + grades[0][1] + grades[0][2] + grades[0][3] + grades[0][4])/len(grades[0])
B = (grades[1][0] + grades[1][1] + grades[1][2] + grades[1][3])/len(grades[1])
J = (grades[2][0] + grades[2][1] + grades[2][2] + grades[2][3])/len(grades[2])
K = (grades[3][0] + grades[3][1] + grades[3][2])/len(grades[3])
S = (grades[4][0] + grades[4][1] + grades[4][2] + grades[4][3] + grades[4][4])/len(grades[4])
# A, B, J, K, S - средний балл каждого ученика
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students)
my_list.sort()
dict = {my_list[0]: A, my_list[1]: B, my_list[2]: J, my_list[3]: K, my_list[4]: S}
print(dict)
# кажется будто вы скажите мне среднее значение переписать порациональнее