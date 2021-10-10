'''Desenvolva
um algoritmo que solicite ao usuário o preço de um produto e um percentual de
desconto aser aplicado a ele. Calcule e exiba o valor do desconto e o preço
final do produto.'''

preco = float(input('Qual o valor do produto? R$ '))
porcentagem = int(input('Qual a porcentagem de desconto? (0-100%) '))

desconto = ((preco * porcentagem)/100)
valor = preco - desconto
print('O desconto dado foi de R${:.2f}, portanto o valor final a ser pago é R${:.2f}.'.format(desconto,valor))

