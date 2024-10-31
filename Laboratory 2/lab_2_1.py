money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
se = money_capital+salary
m = 0  # месяцев
c = se
x=0

while c > x:

    x = spend - salary
    m = m + 1
    money_capital = money_capital - x
    spend = spend * (1 + increase)
 #   print(spend)

    c = money_capital


print("Количество месяцев, которое можно протянуть без долгов:", m)
