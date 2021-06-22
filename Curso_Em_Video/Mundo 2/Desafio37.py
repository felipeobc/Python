Num = int(input('Escreva um numero Inteiro: '))

print('Numero escolhido: {}'.format(Num))

print('(1) - Binario, (2) - Octal (3) - Hexadecimal')
print('Que tipo de Bse voce quer converter? ')
Base = int(input('Escolha uma opção: '))

if Base == 1:

    print('BINARIO: {}'.format(bin(Num)))

elif Base == 2:

    print('Octal: {}'.format(oct(Num)))

else:

    print('Octal: {}'.format(hex(Num)))