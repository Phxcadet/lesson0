set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'hello', True, (1, 2 ,3)} # {} множество хранит УНИКАЛЬНЕЫЕ значения
# в множестве могут быть разные типы данных
print(set_)
list_ = [1, 1, 1, 1, 2, 3, 2, 2]
list_ = set(list_) # set() делает из списка множество
print(list_) # множество не соержит повторяющиеся элементы
# в множестве нельзя обратиться к элементу  по индексу
list_.discard(1) # .discard() удаляет из множества уникальный элемент
print(list_)
list_.remove(2)
print(list_) # .remove() тоже удаляет
# отличия discard: не выдаст ошибку если элемента нет в множестве
list_.add(5) # .add добавляет в множество уникальный элемент
print(list_)
