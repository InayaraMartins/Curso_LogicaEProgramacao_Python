'''Crie um algoritmo que receba um
valor do tipo inteiro via teclado
No entanto, o programa só deve
aceitar, obrigatoriamente,
valores inteiros e positivos
Qualquer valor negativo, ou igual a zero,
deve ser rejeitado pelo programa e um
novo valor deve ser solicitado'''

n = int(input('Digite um valor inteiro e positivo: '))
while n <= 0:
    n = int(input('Digite um valor inteiro e positivo: '))

print ('Você digitoi {}. Encerrando ....'. format(n))