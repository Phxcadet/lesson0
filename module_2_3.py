my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_ = len(my_list)
a = 0
while a <= len_ - 1:
    b = my_list[a]
    if b > 0:
        print(b)
    a = a + 1
    if b < 0:
        break
