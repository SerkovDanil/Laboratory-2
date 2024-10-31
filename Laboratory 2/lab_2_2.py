salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
m = 0  # месяцев
money_capital = 0
while m < months:
    c = salary - spend
    money_capital = money_capital + c
    spend = spend * (1 + increase)
    m = m+1

money_capital = int(money_capital * (-1))

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital )
