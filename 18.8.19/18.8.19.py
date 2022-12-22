ticket = int(input('Введите количество билетов: '))
age = 0
cost = 0
for i in range (ticket):
    age = int(input(('Введите возраст посетителя: ')))
    if 1 <= age <= 17:
        cost += 0
    elif 18 <= age <= 24:
        cost += 990
    else: cost += 1390
if ticket > 3:
    cost = cost*0.9
print('Итоговая стоимость:', int(cost))