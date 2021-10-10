s = float(input('Qual é seu salário? '))
a = int(input('Qual é seu tempo de empresa? '))
if a >= 5:
    bonus = (s * (20/100))
else:
    bonus = (s * (10/100))

print('Sua bonificação sera de R$ {}.'.format(bonus))

