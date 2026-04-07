ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    if not str_:
        return False
    for numbers in str_:
        if numbers not in ALLOW_SYMBOLS:
            return False
    return True
    # TODO проверить что в строку входят только символы 1 и 0


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
