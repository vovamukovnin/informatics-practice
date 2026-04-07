# TODO реализовать функцию count
def count(list_, argument):
    numbers = list_.count(argument)
    return numbers



list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
