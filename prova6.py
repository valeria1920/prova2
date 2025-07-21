n=int(input('digite um numero'))
soma=sum(i for i in range (1, n+1) if i %2==0)
print(f' soma dos numeros pares: {soma}')