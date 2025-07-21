def contar_vogais(frase):
    vogais="AEIOU"
    contador=0
    for letra in frase:
        if letra in vogais:
            contador+=1
            return contador
        frase=input('digite uma frases:')
        numero_de_vogais=contar_vogais(frase)
        print(f'a frase contem {numero_de_vogais}')