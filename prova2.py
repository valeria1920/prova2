total=float(input('digite o valor da compra'))
pago=float(input('digite o valor pago'))

if total< total:
    falta= total-pago
    print(f'valor insuficiente, faltam {falta:.2}')
elif pago==total:
    print(f'pagamento exato, não há troco')
else:
    troco= pago-total
    print(f'troco: R${troco}')