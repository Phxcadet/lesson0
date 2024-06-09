grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
middle = []
middle.append(sum(grades[0]) / len(grades[0]))
middle.append(sum(grades[1]) / len(grades[1]))
middle.append(sum(grades[2]) / len(grades[2]))
middle.append(sum(grades[3]) / len(grades[3]))
middle.append(sum(grades[4]) / len(grades[4]))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students)
my_list.sort()
dictionary = dict(zip(my_list, middle))
print(dictionary)

