from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print(''' Suas opcções: 
[ 1 ] - PEDRRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA
''')

jogador = int(input('Qual a sua jogada: '))
print('-=' *10)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=' *10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador ==2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador ==1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

