Numero1 = int(input('Digiti um numero: '))
Numero2 = int(input('Digiti outro numero: '))

print('''Escola uma opção
[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão ''')
opcao = int(input('Digie uma opção: '))

if opcao == 1:
    print('SOMA')
    print('{} + {} = {}'.format(Numero1, Numero2, Numero1 + Numero2))
elif opcao == 2:
    print('SUBTRACAO')
    print('{} - {} = {}'.format(Numero1, Numero2, Numero1 - Numero2))
elif opcao == 3:
    print('MULTIPLICAÇÂO')
    print('{} x {} = {}'.format(Numero1, Numero2, Numero1 * Numero2))
elif opcao == 3:
    print('DIVISAO')
    print('{} / {} = {}'.format(Numero1, Numero2, Numero1 - Numero2))
else:
    print('Opção incorreta')
