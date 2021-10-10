'''Escreva um algoritmo que
realize um login em um
sistema
O usuário deve informar
seu nome e senha'''

while True:
    login = input('LOGIN: ').upper().lstrip()
    if login != 'INAYARA':
        continue
    senha = input('SENHA: ')
    if senha == 'Uninter':
        break
print('Acesso liberado!')