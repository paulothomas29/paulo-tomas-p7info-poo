def primo(p):
    contador = 0
    for i in range (1,p+1):
        if p%i==0:
            contador = contador+1
    if  contador==2:
        return True
    else:
        return False

def somador(n): 
    contador = 0
    soma = 0
    inputNum = 2
    primos = []
    while True:
        if primo(inputNum):
            contador = contador + 1
            soma = soma + inputNum
            primos.append(inputNum)
        inputNum = inputNum + 1
        if contador == n:
            break
    return (soma,primos)

inputNum = input("Informe um número INTEIRO não NEGATIVO:")
soma, parcela = somador(int(inputNum))
if int(inputNum) >= 0:
    print("Quando n for = {0}, o resultado é {s}, sendo as parcelas {p}. ".format(int(inputNum), s= soma, p = parcela))