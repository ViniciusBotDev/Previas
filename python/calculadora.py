continuar = "s"

while continuar == "s" or continuar == "S" :
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))

    print("Operações númericas:")
    print("[1] Para Somar ")
    print("[2] Para Subtrair ")
    print("[3] Para Multiplicar ")
    print("[4] Para Dividir")

    op = (input("Escolha a operação (1/2/3/4): "))

    if op == "1" :
        print("Resultado", num1 + num2) 
    elif op == "2" :
        print("Resultado", num1 - num2) 
    elif op == "3" :
        print("Resultado", num1 * num2) 
    elif op == "4" :
        if num2 != 0:
            print("Resultado", num1 / num2)
        else :
                print("Erro de calculo")  
    continuar = input("Quer continuar? [S/N]")  
print("Fim!")
