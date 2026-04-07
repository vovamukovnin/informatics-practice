# TODO Напишите функцию для поиска индекса товара
def func(list_items, item):
    for find_item in list_items:
        if find_item == item:
            index_item = list_items.index(find_item)
            return index_item
            break


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for item in ['банан', 'груша', 'персик']:
    index_item = func(items_list, item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{item}' не найден в списке.")
