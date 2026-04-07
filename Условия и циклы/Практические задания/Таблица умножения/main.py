# TODO Распечатать таблицу умножения
size = 9
for i in range(2, size+1):
    for j in range(2, size+1):
        result = i * j
        end = " " if j != size else ""  # Не печатать пробел для последнего столбца
        print(f"{result:2}", end=end)
    print()