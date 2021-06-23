PrecoNormal = float(input('Valor normal do produto R$: '))

print('Escolha uma forma de pagamento')
print("(1) - A vista dinheiro, (2) - A vista no cartão, (3) - Parcelado")
FormaPagamento = int(input('Escolha uma forma de pagamento: '))

if FormaPagamento == 1:
    print('A vista dinheiro')
    PrecoFinal = (PrecoNormal * 10)/100
    print('Valor a ser pago com 10% de desconto R$: {}'.format(PrecoNormal - PrecoFinal))
elif FormaPagamento == 2:
    print('A vista cartão')
    PrecoFinal = (PrecoNormal * 5)/100
    print('Valor a ser pago com 10% de desconto R$: {}'.format(PrecoNormal - PrecoFinal))
elif FormaPagamento == 3:
    print('Parcelado')
    NumeroParcela = int(input('Informe o numero de parcela: '))
    if NumeroParcela <= 2:
        print('O valor em 2x R$: {}'.format(PrecoNormal/2))
    else:
        PrecoFinal = (PrecoNormal * 20)/100
        print('Valor a ser pago com 10% de desconto R$: {}'.format((PrecoNormal + PrecoFinal)/2))
        