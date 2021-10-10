cont = 0
p1 = input('Telefonou para a vítima? ').upper().lstrip()
if p1 == 'SIM':
    cont = cont + 1
p2 = input('Esteve no local do crime? ').upper().lstrip()
if p2 == 'SIM':
    cont = cont + 1
p3 = input('Mora perto da vítima? ').upper().lstrip()
if p3 == 'SIM':
    cont = cont + 1
p4 = input('Devia para a vitima? ').upper().lstrip()
if p4 == 'SIM':
    cont = cont + 1
p5 = input('Já trabalhou com a vítima? ').upper().lstrip()
if p5 == 'SIM':
    cont = cont + 1

if cont == 2:
    print('Pessoa suspeita')
elif cont == 3 or cont == 4:
    print('Pessoa Cumplice')
elif cont == 5:
    print('Pessoa Assacina')
else:
    print('Inocente')