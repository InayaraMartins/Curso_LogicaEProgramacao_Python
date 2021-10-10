'''Escreva um algoritmo em Python
que calcule a tabuada de todos os
números de 1 até 10, e, para cada
número, vamos calcular a tabuada
multiplicando-o pelo intervalo de
1 até 10'''

# 2 for
for c in range(1,11,1):
    print('TABUADA DO {}:'.format(c))
    for i in range(1,11,1):
        print('{} X {} = {}'.format(c,i,c * i))
    print('='*10)

# 2 while
'''i = 1
while i <= 10:
    print('TABUADA DO {}:'.format(i))
    j = 1
    while j <= 10:
        print('{} X {} = {}'.format(i, j, i * j))
        j = j + 1
    print('='*10)
    i = i + 1'''



