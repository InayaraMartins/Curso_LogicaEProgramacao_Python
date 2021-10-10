'''Escreva as seguintes expressões algébricas
em linguagem Python:
a) O somatório dos 5 primeiros números
inteiros e positivos
b) A média entre 23, 19 e 31
c) O número de vezes que 73 cabe em 403
d) A sobra quando 403 é dividido por 73
e) 2 elevado à 10ª potência
f) O valor absoluto da diferença entre 54 e
57
g) O menor valor entre 34, 29 e 31'''

print(1+2+3+4+5)
print((23+19+31)/3)
print(403//73)
print(403%73)
print(2**10)
print(abs(54-57))
print(min(34,29,31))


'''Atribuição
Escreva as expressões em Python para:
a) Atribuir o valor inteiro 3 à variável a
b) Atribuir o valor 4 à variável b
c) Atribuir à variável c o valor da expressão
a*a + b *b
'''

a = 3
b = 4
c = (a*a) + (b*b)

'''Strings
Execute as seguintes atribuições:
s1 = ‘ ant
s2 = ‘ bat
s3 = ‘ cod
Agora, utilizando operadores + e *, crie as saídas
a seguir:
a) ant bat cod
b) ant ant ant ant ant ant ant ant ant ant
c) ant bat bat cod cod cod
d) ant bat ant bat ant bat ant bat ant bat ant bat
ant bat
e) batbatcod batbatcod batbatcod batbatcod
batbatcod'''

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1+ ' '+ s2+ ' '+ s3)
print(10* (s1 + ' '))
print(s1 + ' ' + 2* (s2 + ' ') + 3* (s3 + ' '))
print(7 *(s1 + ' ' + s2 +' '))
print(s2*2,s3)
print(5*(s2*2+s3+ ' '))

