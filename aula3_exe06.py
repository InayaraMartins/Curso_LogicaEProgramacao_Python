nome = str(input('Qual seu nome? ')).upper().lstrip()
idade = int(input('Qual a sua idade? '))

if nome == 'VINICIUS':
    print('Olá, Vinícius')
else:
    if idade <=18:
        print('Você não é o Vinícius e é de menor!')
    elif idade >= 18 and idade <= 100:
        print('Você não é o Vinícius e você é de maior!')
    else:
        print('Essa pessoa provavelmente não existe!')
