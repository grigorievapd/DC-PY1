def delete(list_, index=None):
    if len(list_) == 0:
        return 'Список пуст'
    elif index is not None:
        if abs(index) <= len(list_)-1:
           list_a = list_[:index]
           list_b = list_[index+1:]
           list_a.extend(list_b)
           return list_a
        return 'Индекс не входит в список'
    list_.pop()
    return list_
    ...  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
