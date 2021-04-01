money = float(input('Введите сумму '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for i in per_cent.values():
    deposit.append(i*money/100)
print('Ваши деньги: ', money)
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))