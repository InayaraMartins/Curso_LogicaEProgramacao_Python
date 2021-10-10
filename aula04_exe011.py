'''1. Reescreva o programa dos números pares, mas agora em vez de obter
números pares, escreva na tela os 10 primeiros valores múltiplos de 3.'''

inicio = int(input('Qual o valor deseja iniciar? '))
fim = int(input("Qual valor deseja terminar? "))

c = 1
x = inicio
while c <= 10 and x <= fim:
    if x % 3 == 0:
        print(x)
        c = c + 1
    x = x + 1
