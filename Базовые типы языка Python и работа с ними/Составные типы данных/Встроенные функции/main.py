digit = '495184'
list_digit = []
for a in digit:
    a = int(a)
    list_digit.append(a)
  # TODO сформировать список цифр
print(list_digit)

print("Сумма цифр", sum(list_digit))  # TODO сумма цифр
print("Количество цифр",len(list_digit))  # TODO количество цифр
print("Минимальная цифра", min(list_digit))  # TODO минимальная цифра
print("Максимальная цифра",max(list_digit))  # TODO максимальная цифра
print("Среднее арифметическое цифр", round(sum(list_digit)/len(list_digit), 2))  # TODO среднее арифметическое цифр
