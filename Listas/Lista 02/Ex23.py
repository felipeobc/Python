ano = int(input('Digite o ano que deseja: '))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("{} esse ano é Bissesto".format(ano))
else:
    print('{} Não  é bissesto'.format(ano))

