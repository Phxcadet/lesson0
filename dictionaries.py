phone_book = {'Denis': 88005553535, 'Max': 88005758493} # первое это ключ: второе значение словарик в {}
# Ключом может быть ТОЛЬКО неизменяемый объект
# на месте данных может быть изменяеое
print(phone_book)
print(phone_book['Denis']) # можно выписывать элементы
phone_book['Denis'] = 2441414141 #словарь - изменяемая структура!
print(phone_book)
phone_book['Anton'] = 29415139513 # добавляет несуществующий к словарю
print(phone_book)
del phone_book['Max'] # del удаляет элемент из словаря
print(phone_book)
phone_book.update({'Sasha': 423141414,
                   'Alex': 694262962}) #.update добавляет несколько элементов сразу
print(phone_book)
# словарь - неупорядоченная коллекция!
print(phone_book.get('Denis'))
print(phone_book.get('Valya')) # .get его отличие в том, что если нет элемента на выходит будет None (ничего)
# print(phone_book['Valya']) дает ошибку
print(phone_book.get('Kamila', 'Такого ключа нет')) # через запятую на отсутствующий элемент заменяет none на другое
a = phone_book.pop('Anton') # .pop удаляет ключ, и сохраняет значение в переменную,
# также работает для списка
print(phone_book)
print(a)
list_ = [1, 2, 3, 4]
b = list_.pop(0)
print(b)
print(phone_book.keys()) # .keys метод позволяет получить колекцмю из ключей в словаре
print(phone_book.values())# .values возвращает значения
print(phone_book.items()) # .items возвращает пары
# в веб разработке много словарей
