peso=float(input('digite o seu peso'))
altura=float(input('digite a sua altura'))
imc=peso/(altura**2)
print(f'imc: {imc}')
if imc<18.5:
    print('classificacao: abaixo do peso')
elif imc<25:
    print('classificacao: peso normal')
elif imc<30:
    print('classificacao: assima do peso')
elif imc<35:
    print('classificacao: obsidade grau 1')
elif imc<40:
    print('classificacao: obesidade grau 2')
else:
    print('classificacao: obesidade gra 3')