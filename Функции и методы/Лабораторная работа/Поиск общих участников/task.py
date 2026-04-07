# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, separator = ","):
    str1 = str1.split(separator)
    str2 = str2.split(separator)
    group = set(str1).intersection(str2)
    return list(sorted(group))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(participants_first_group, participants_second_group)
# TODO Провеьте работу функции с разделителем отличным от запятой
