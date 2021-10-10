'''Escreva um programa que calcule o preço a
pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o
tipo de instalação: R para residências, I para
indústrias e C para comércios

Residencial Até 500 0,40 ; Acima de 500 0,65
Comercial   Até 1000 0,55; Acima de 1000 0,60
Industrial  Até 5000 0,55; Acima de 5000 0,60'''

qtd = float(input('Qual a quantidade de energia (kWh) consumida? '))
print('='*10,'TIPO DE INSTALAÇÃO', '='*10)
print('''
Residencial: (R)
Comercial: (C)
Industrial: (I)''')
print('='*30)

inst = input('Qual o tipo de instalação? ').upper()

if inst == 'R':
    if qtd <= 500:
        valor = 0.40
    else:
        valor = 0.65
elif inst == 'C':
    if qtd <= 1000:
        valor = 0.55
    else:
        valor = 0.60
elif inst == 'I':
    if qtd <= 5000:
        valor = 0.55
    else:
        valor = 0.60
else:
    print('Escolha inválida!')
print('O preço a pagar ela energia {} é R${:.2f}.'.format(inst, valor * qtd))
