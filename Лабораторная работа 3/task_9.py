salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
need = 0
# TODO Оформить решение
for i in range(1, months+1):
    if i == 1 :
        need_money -= spend
        need_money += salary
    elif i!= months+1:
        spend *= 1+increase
        need_money -= spend
        need_money+=salary
    else:
        spend *= 1+increase
        need_money -= spend
        need_money+=salary


print(round(abs(need_money)))
