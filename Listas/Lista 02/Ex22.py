ideda = int(input('Qual a sua Idade: '))
tempoServicos = int(input('Quanto tempo de serviço  voce te: '))

if ideda >= 65:
    print("voce pode se aposentar!")
elif tempoServicos > 30: 
    print("voce pode se aposentar!")
elif ideda > 60 and tempoServicos >= 25:
    print("voce pode se aposentar!")
else:
    print("Voce nao pode se aposentar")
    