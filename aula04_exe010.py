'''Faça um programa para exibir na tela número de 10 a 1.000.
Modifique-o também para exibir na tela uma contagem regressiva do lançamento de um foguete,
iniciando em 10 até 0 e escrevendo, após o 0, a palavra: fogo!'''

'''x = 10
while x < 1001:
    print(x)
    x = x + 1'''

import time
print('Iniciando contagem para lançamento de foguete...')
x = 10
while x > 0:
    print ('{} ...'. format(x))
    time.sleep(1)
    x = x - 1
print('FOGUETE LANÇADO!')
