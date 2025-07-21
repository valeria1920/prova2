valores=[True,False,True,False,True]
contagem_true=0
contagem_false=0
for valor in valores:
    if valor:
        contagem_true+=1
    else:
        contagem_false+=1
        print(f'numero de true:contagem_true')
        print(f'numero de false:contagem_false')