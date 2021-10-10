'''Expressões booleanas
Escreva as seguintes expressões booleanas
em linguagem Python:
a) O somatório de 2 com 2 é menor do que 4
b) O valor 7 // 3 é igual a 1 + 1
c) A soma de 3 elevado ao quadrado com 4
elevado ao quadrado é igual a 25
d) A soma de 2, 4 e 6 é maior do que 12

a) 1387 é divisível por 19
b) 31 é par
c) O menor valor entre: 34, 29 e 31 é menor
do que 30'''

''' minha resolução
somatorio = 2 + 2
res = somatorio < 4
print(res)'''

print(2 + 2 < 4)

print((7// 3)==(1+1))

print(((3**2) + (4**2)) == 25)

print((2 +4 +6)> 12)

print(1387 % 19 == 0)

print(13 % 2 == 0)

print(min(34,29,31) < 30)

'''Condicionais simples
Traduza as afirmações a seguir para condicionais
em Python:
a) Se idade é maior que 60, escreva: “Você tem
direitos aos benefícios”
b) Se dano é maior do que 10 e escudo é igual a
0, escreva: “Você está morto!”
c) Se pelo menos uma das variáveis booleanas
norte, sul, leste e oeste resultarem em True ,
escreva: “Você escapou!”'''

idade = int(input('Qual sua idade? '))
if idade > 60:
    print('Você tem direitos aos benefícios')

dano = int(input('Digite o dano: '))
escudo = int(input('Digite o escudo: '))
if dano > 10 and escudo == 0:
    print('Você esta morto!')

'''if norte == True or sul == True or leste == True or oeste == True: # if norte or sul or leste or oeste:
    print('Você escapou!!')'''

''' Condicional composta 
Traduza as afirmações a seguir para
condicionais em Python:
a) Se ano é divisível por 4, escreva: “Pode ser
um ano bissexto”. Caso contrário, escreva:
“Definitivamente não é um ano bissexto
b) Se ambas as variáveis booleanas cima e
baixo forem True , escreva: “Decida se!”,
caso contrário, escreva: “Você escolheu
um caminho!”'''

ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

print('''Escola um caminho:
1 => Ir para cima
2 => Ir para baixo''')
c1 = int(input('Caminho: '))
c2 = int(input('Confirme o caminho: '))
if (c1 == 1 and c2 == 2) or (c1 == 2 and c2 == 1):
    print('Decida-se!')
else:
    print('Você escolheu um caminho')
