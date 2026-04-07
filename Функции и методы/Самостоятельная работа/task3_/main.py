def delete(list_, index= -1):
    list_.pop(index)  # TODO реализовать функцию удаления элемента из списка по индексу
    return list_

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
