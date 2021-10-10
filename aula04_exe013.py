'''Escreva
um algoritmo que leia dois valores e imprima na tela o resultado da
multiplicação de ambos.Entretanto, para calcular a multiplicação, utilize
somente operações de soma e subtração (Menezes; Nilo, p. 88).
Lembrando que uma multiplicação pode ser considerada
como um somatório sucessivo. Utilize essa lógicapara construir seu algoritmo.'''


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))

soma = 0
cont = 1
while cont <= n2:
    soma = soma + n1
    cont = cont + 1

print('A multiplicação de {} X {} é igual a: {}'.format(n1, n2, soma))
