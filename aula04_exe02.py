'''Escreva um algoritmo que imprima
na tela somente valores dentro de
um intervalo especificado pelo
usuário e que sejam número pares'''


v1 = int(input('Escreva o início do seu intervalo: '))
v2 = int(input('Escreva o final do seu intervalo: '))
cont = v1
while cont <= v2:
    if cont % 2 == 0:
        print(cont)
    cont = cont + 1







