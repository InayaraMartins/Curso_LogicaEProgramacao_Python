'''Escreva um algoritmo que calcule
a sua média de notas em
determinada disciplina
Vamos assumir que a média final
é dada pela média aritmética de
cinco notas digitadas'''

cont = 1
soma = 0
while cont <= 5:
    n = float(input('Digite a {}º nota: '.format(cont)))
    cont = cont + 1
    soma = soma + n
media = soma /5
print('A média final é: {:.2f}'.format(media))