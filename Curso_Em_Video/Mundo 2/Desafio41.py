ano = int(input('Qual Ano de Nascimento do atleta: '))

idade = 2021 - ano

if idade >= 10 and idade < 20:
    print('Você é adolescente')
elif idade >= 20 and idade < 30:
    print('Você é jovem')
elif idade >= 30 and idade <= 100:
    print('Você é adulto')
else:
    print('Valor não encontrado!')

    