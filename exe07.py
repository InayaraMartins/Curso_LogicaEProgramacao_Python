'''Faça um algoritmo que receba três valores, representando os lados de um triângulo
fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
a) Equilátero (três lados iguais)
b) Isósceles (dois lados iguais)
c) Escaleno (três lados diferentes)'''

a = float(input('Digite um valor de um lado: '))
b = float(input('Digite outro valor do lado: '))
c = float(input('Digite o terceiro valor do lado: '))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print('Os valores {} , {} e {} podem formar um triângulo!'.format(a, b, c))
    if a == b and a == c and b == c:
        print('O triângulo formado é Equilátero.')
    elif (a != b) and (a != c) and (b != c):
        print('O triângulo formado é Escaleno.')
    else:
        print('O triângulo formado é Isósceles.')
else:
    print('Os valores {} , {} e {} não podem formar um triângulo!'.format(a, b, c))
