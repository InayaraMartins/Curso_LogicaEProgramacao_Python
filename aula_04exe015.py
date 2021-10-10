'''Escreva um algoritmo que leia números inteiros via teclado. Somente valores positivos
devem ser aceitospelo programa (Menezes; Nilo, p. 91).
O programa deve receber números até que o usuário digite zero.
Ao final da execução, informe a média dos valores digitados. Realize a implementação com as instruções
break e continue e trabalhe com operaçõeslógicas Truthy e False. Não esqueça de empregar também operadores especiais de
atribuição.'''


soma = 0
cont = 0
n = 0
while True:
    n = int(input('Digite um valor inteiro e positivos: '))
    if n < 0:
        continue
    if not n: #if n == 0:
        break
    soma = soma + n
    cont = cont + 1
media = soma / cont
print('A média é {:.2f}'.format(media))
