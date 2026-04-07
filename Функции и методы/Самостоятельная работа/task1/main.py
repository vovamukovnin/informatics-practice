# TODO реализовать функцию
def remove_whitespace(str_):
    new_str_ = str_.split(" ")
    list = []
    for word in new_str_:
        if word:
            list.append(word)
    str_1 = ' '.join(list)
    return str_1


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
