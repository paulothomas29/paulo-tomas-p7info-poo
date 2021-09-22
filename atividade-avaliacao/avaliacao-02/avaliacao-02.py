texto = 0
separador = "-"
while True:
    frase = input("Digite a frase desejada: ").split()
    tamanho = []
    
    for p in frase:
        tamanho.append(str(len(p)))
        if len(p) >= texto:
            texto = len(p)
            maiorPalavra = p
    print(separador.join(tamanho))

    end = str(input("Digite 0 para encerrar o programa ou pressione ENTER para prosseguir:"))
    if end == "0":
        break

print()
print("A maior palavra é: %s" % maiorPalavra)