'''Crie um programa que calcule a tabuada de um número escolhido pelo
usuário. Imprima na tela atabuada desse número de 1 a 10. Ao realizar a
impressão na tela, mostre os valores formatados conformea seguir.
Exemplo com a
tabuada do 5:
1x5=5, 2x5=10, 3x5=15...'''

n = int(input('Escolha o número que deseja vizualizar a TABUADA: '))

j = 0
while j <= 10:
    print('{}  X  {}  = {}'. format(j, n,n*j))
    j = j + 1
