'''Escreva um algoritmo que leia dois valores
numéricos e que pergunte ao usuário qual
operação ele deseja realizar: adição (+),
subtração (-), multiplicação (*) ou divisão
(/). Exiba na tela o resultado da operação
desejada (exercício da apostila aula 3)'''

n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
print('='*25)
print('''CALCULADORA:
adição: (+)
subtração (-)
multiplicação (*) 
divisão (/)''')
print('='*25)
operacao= (input('Qual operação você deseja realizar? '))

if operacao == '+':
    print('A adição de {} e {} é {}'.format(n1,n2, n1+n2))
elif operacao == '-':
    print('A subtração de {} e {} é {}'.format(n1,n2, n1-n2))
elif operacao == '*':
    print('A multiplicação de {} e {} é {}'.format(n1,n2, n1*n2))
elif operacao == '/':
    print('A divisão de {} e {} é {}'.format(n1,n2, n1/n2))
else:
    print('escolha inválida!')

print('Encerrando o programa')