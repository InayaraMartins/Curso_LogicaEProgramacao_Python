print(''' Lista de produtos:
1: Maçâ
2: Laranja
3: Lanana''')

p = int(input('Qual produto você deseja comprar?  '))
u = int(input('Quantas unidades você deseja comprar? '))

if p == 1:
    valor = u * 2.30
    print('O valor total a pagar por {} maçãs é de R${:.2f}'.format(u,valor))
elif p ==2:
    valor = u * 3.60
    print('O valor total a pagar por {} laranjas é de R${:.2f}'.format(u, valor))
elif p == 3:
    valor = u * 1.85
    print('O valor total a pagar por {} bananas é de R${:.2f}'.format(u,valor))
else:
    print('Produto inexistente!')
