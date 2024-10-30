money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
se = money_capital+salary
m = 0  # месяцев
c = se

while c > 0:

    c = salary - spend * (1 + m * increase) + money_capital
    money_capital = money_capital + salary - spend * (1 + m * increase)
    m = m+1


print("Количество месяцев, которое можно протянуть без долгов:", m)
