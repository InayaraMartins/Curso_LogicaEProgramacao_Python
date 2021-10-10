'''Escreva um algoritmo que fique
recebendo frases ou palavras
digitadas pelo usuário
Encerre o algoritmo quando a
palavra sair for digitada'''

print('Digite uma frase ou palavra, caso queira encerrar digite SAIR')
while True:
    frase = input('Frase:').upper().lstrip()
    print(frase)
    if frase == 'SAIR':
        break
print('Você pediu para Sair. Encerrando....')