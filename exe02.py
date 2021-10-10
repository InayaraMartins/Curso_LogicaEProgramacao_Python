'''Desenvolva
um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos
e desegundos. Calcule o total de segundos resultante e imprima na tela para o
usuário.'''

n1 = int(input('Quantos dias: '))
n2 = int(input('Quantas horas: '))
n3 = int(input('Quantos minutos: '))
n4 = int(input('Quantos segundos: '))

dia = n1 * 86400
hora = n2 * 3600
minutos = n3 * 60

res = n4 + dia + hora + minutos

print('O total de segundos calculados é : {}.'.format(res))
