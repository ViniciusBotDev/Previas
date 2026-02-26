from time import sleep
continuar = False
while not continuar:
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))
    print("""Operações númericas:
    [ 1 ] Para Somar
    [ 2 ] Para Subtrair
    [ 3 ] Para Multiplicar
    [ 4 ] Para Dividir
    [ 5 ] Para novos números
    [ 6 ] Sair do programa""")
    opção = int(input("Escolha a operação (1/2/3/4/5/6): "))
    if opção == 1:
        print("Resultado", num1 + num2)
        sair = input("Quer sair? [S/N]:  ").strip().upper()
        if sair == 'S':
            break
    elif opção == 2:
        print("Resultado", num1 - num2) 
    elif opção == 3:
        print("Resultado", num1 * num2) 
    elif opção == 4:
        if num2 != 0:
            print("Resultado", num1 / num2)
        else :
                print("Erro de calculo")  
    elif opção == 5:
        continuar == True
    elif opção == 6:
        print('SAINDO..')
        sleep(1)
        break
print("Fim!")
