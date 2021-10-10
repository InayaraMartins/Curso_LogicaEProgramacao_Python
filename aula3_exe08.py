v= float(input('Qual o valor total da compra? R$ '))
print('''FORMAS DE PAGAMENTO

à vista – 1;
em 3x – 2;
em 5x – 3;
em 10x – 4.''')

pag = int(input('Escolha a forma de pagamento: '))
if pag == 1:
    des = (v * (5/100))
    pf = v - des
    vezes = 'à vista'
elif pag == 2:
    pf = v
    vezes = '2 vezes'
 elif pag == 3:
    acre = (v * (2/100))
    pf = v + acre
    vezes = '3 vezes'
elif pag == 4:
    acre = (v * (8 / 100))
    pf = v + acre
else:
    print('Opção inválida!')
print('O total a ser pago será de R$ {}'. format(pf))