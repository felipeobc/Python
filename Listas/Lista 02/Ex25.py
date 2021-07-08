print('Equação do 2°Grau')
a = float(input('O valor de A'))
b = float(input('O valor de B'))
c = float(input('O valor de C'))

delta = pow(b,2) - 4*a*c

if a == 0:
    print('Não é equação de segundo grau')
elif delta < 0:
    print('Nao existe raiz.')
elif delta == 0:
    print('Raiz única')
elif delta >= 0:
    print('Raiz dupla')