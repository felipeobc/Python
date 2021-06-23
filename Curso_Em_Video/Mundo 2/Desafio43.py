peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))

IMC = peso/(pow(altura,2))

print(IMC)

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC > 18.5 and IMC <= 25:
    print('Peso ideal')
elif IMC > 25 and IMC <= 30:
    print('Sobrepeso')
elif IMC > 30 and IMC <= 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade II')
