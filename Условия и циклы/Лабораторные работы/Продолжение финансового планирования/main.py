salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 0  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while months != 10:
    months += 1
    money = salary - spend
    spend = spend + spend*increase
    need_money = money *(-1)
    money_capital = money_capital + need_money

money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
