'''Escreva um algoritmo que calcule
a média dos números pares de
1 até 100 (1 e 100 inclusos).
Implemente o laço usando for'''

soma = 0
cont = 0
for c in range(1,101):
    if c % 2 == 0:
        soma = soma + c
        cont = cont + 1
media = soma/cont

print('A média dos valores pares de 1 até 100 é: {}.'.format(media))

