ano = int(input('Qual Ano de Nascimento: '))

Idade = 2021 - ano

print('Idade: {}'.format(Idade))
if Idade < 18:
    print('Ainda vai se alistar')
elif Idade == 18:
    print('Hora de se Alistar')
else:
    print('Passou da hora de se alistar')