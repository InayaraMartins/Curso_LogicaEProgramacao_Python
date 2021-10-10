'''Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final. Para
este intervaloespecificado pelo usuário, calcule e mostre na tela (Puga, p.70):
a) A quantidade de números inteiros e positivos;
b) A quantidade de números pares;
c) A quantidade de números ímpares;
d) A respectiva média de cada um dos itens anteriores.
Será necessário criar uma variável distinta para cada somatório, para cada quantidade e para cada médiasolicitada.'''

inicio = int(input('Digite um valor inicial: '))
final = int(input('Digite outro valor final: '))

qtd_positivos = 0
qtd_pares = 0
qtd_imapar = 0
soma_positivo = 0
soma_pares = 0
soma_imapar = 0
cont = inicio
if cont < final:
    while cont <= final:
        if cont > 0:
            qtd_positivos = qtd_positivos + 1
            soma_positivo = soma_positivo + cont
        if cont % 2 == 0:
            qtd_pares = qtd_pares + 1
            soma_pares = soma_pares + cont
        else:
            qtd_imapar = qtd_imapar + 1
            soma_imapar = soma_imapar + cont
        cont = cont + 1
    media_positivo = soma_positivo/qtd_positivos
    media_pare = soma_pares/qtd_pares
    media_impar = soma_imapar/qtd_imapar
    print('Quantidade de valores positivos: {}'.format(qtd_positivos))
    print('Média valores positivos: {}'.format(media_positivo))
    print('Quantidade de valores pares: {}'.format(qtd_pares))
    print('Média valores pares: {}'.format(media_pare))
    print('Quantidade de valores impares: {}'.format(qtd_imapar))
    print('Média valores impares: {}'.format(media_impar))
else:
    print('Você digitou um valor inicial maior ou igual ao final. Encerrando programa...')