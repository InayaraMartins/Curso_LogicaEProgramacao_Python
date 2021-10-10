'''Desenvolva
um algoritmo que converta uma temperatura em Celsius (C) para Fahrenheit (F). A
equação deconversão é:'''

c = float(input('Digite uma temperatura em Celsius(C): '))
f = ((9 * c)/5)+32
print('A temperatura de {} Celsius é igual a {} Fahrenheit'.format(c,f))