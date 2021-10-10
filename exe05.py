'''Escreva um programa que pergunte a
quantidade de km percorridos por um
carro alugado pelo usuário, assim como a
quantidade de dias pelos quais o carro foi
alugado. Calcule o preço a pagar, sabendo
que o carro custa R$ 60 por dia e R$ 0,15
por km rodado'''

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))

preco = (60 * dias) + (0.15 * km)

print('O preço a pagar por {} dias de aluguel do carro, considerando {} Km percorrido é de R${:.2f}'.format(dias,km, preco))