ValorCasa = float(input('Qual o Valor da casa: '))
SalarioComprador = float(input('Salario do comprador: '))
AnosPagametos = int(input('Em quantos anos voce quer pagar: '))

ValorPrestacao = ValorCasa / (AnosPagametos * 12)
print('valro da prestação: {} '.format(ValorPrestacao))

PorcetagemSalario = (SalarioComprador *30)/100
print('30 do salario: {}'.format(PorcetagemSalario))

if ValorPrestacao > PorcetagemSalario:
    print('Compra não aprovada')
else:
    print('Compra aprovada')