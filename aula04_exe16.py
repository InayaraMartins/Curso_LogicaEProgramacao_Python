''') Crie um algoritmo para exibir na tela uma contagem regressiva do
lançamento de um foguete,iniciando em 10 até 0 e escrevendo após o 0, a palavra fogo!'''

import time
for n in range(10, -1, -1):
    time.sleep(1)
    print('{}...'.format(n))
time.sleep(0.5)
print('FOGO!!!')