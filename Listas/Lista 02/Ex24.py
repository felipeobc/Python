valorProduto = float(input('Qual é o valor do produto R$:'))

print('''Qual é o estado da venda
(1)SP - São Paulo
(2)MG - Minas Gerais
(3)RJ - Rio de Janeiro
(4)MS - Mato Grosso do Sul''')
Estado = int(input('Escolha uma Opção: '))

if Estado == 1:
    print('São Paulo')
    desconto = (valorProduto*12 / 100)
    print('O valor do produto vai ser R$:{}'.format(valorProduto - desconto))
elif Estado == 2:
    print('Minas Gerais')
    desconto = (valorProduto*7 / 100)
    print('O valor do produto vai ser R$:{}'.format(valorProduto - desconto))
elif Estado == 3:
    print('Rio de Janeiro')
    desconto = (valorProduto*15 / 100)
    print('O valor do produto vai ser R$:{}'.format(valorProduto - desconto))
elif Estado == 4:
    print('Mato Grosso do Sul')
    desconto = (valorProduto*8 / 100)
    print('O valor do produto vai ser R$:{}'.format(valorProduto - desconto))
else:
    print('Por favor escolha uma opção')