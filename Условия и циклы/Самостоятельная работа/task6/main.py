list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_number_index = 0
max_number_value =list_numbers[max_number_index]
# TODO Поменяйте местами значения согласно условию
for current_number_index, current_number_value in enumerate(list_numbers):
    if current_number_value >= max_number_value:
        max_number_value = current_number_value
        max_number_index = current_number_index
list_numbers[-1], list_numbers[max_number_index] = list_numbers[max_number_index], list_numbers[-1]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
