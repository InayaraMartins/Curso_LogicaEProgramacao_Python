try:
    qtd = float(input('Qual a quantidade de gasolina (L): '))

    if qtd > 0:
        if 0 < qtd <=1:
            valor = 7
        elif 1 < qtd <= 10:
            valor = 6.50
        elif qtd > 10:
            valor = 6

        print('O valor a ser pago por  litro de gasolina é {}. O total a ser pagor por {} litros de gasolina é: RS {:.2f}.'.format(valor,qtd, valor * qtd ))
    else:
        print('Opcao invalida')
except:
    print("Opcao invalida try")