Nota1 = float(input('Valor da nota 1: '))
Nota2 = float(input('Valor da nota 2: '))

Media = (Nota1 + Nota2)/2

if Media > 5:
    print('Reprovado')
elif Media == 5 and Media <= 6.9:
    print('Reprovado')
elif Media >=7:
    print('Aprovado')

