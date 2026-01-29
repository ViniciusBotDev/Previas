import sys

saldo = float
voltar = "voltar"
comprar = "comprar"
print("Deseja entrar na loja de PC's? ")
entrar = input("[S/N]  ")
if entrar == "s" or entrar == "S":
    print("\033[1mVoçe entrou na loja de Pc's!\033[0ms")
    print("\033[1mAgora voçe pode escolher algum Pc\033[0ms")
else:
    sys.exit(print("Voçe foi embora "))

saldo = input("Digite qual seu saldo R$")

print(f"Seu saldo agora é R${saldo}")

while voltar == "voltar":
     
    print("Qual voçe deseja escolher? Escolha e veja as configs!")

    op = input("1/2/3/4/5 ou caso queira sair digite: sair  ")
    if op == "sair":
        sys.exit(print("Obrigado por visitar nossa loja!"))
    match op:
        case "1":
            print("PC 1")
            print("Processador: Ryzen 5500X3D")
            print("Placa de Vídeo: RTX 5070 ")
            print("Mémoria Ram: 32GB Ram")
            print("SSD: 1TB ")
            print("Placa mãe: B550 Steel Legend ")
            print("Fonte: 750W Corsair")
            print("Preço: R$7000,00")
            voltar = input("Digite: voltar, se quiser voltar. E se quiser Proseguir digite: comprar,  ")
            if voltar == "comprar":
                print(f"Voçe deseja comprar esse Pc? seu saldo é R${saldo}  ")
                comprar = input("Digite [S/N]  ")
                if comprar == "sim" or comprar == "S" or comprar == "Sim":
                    if saldo >= "7000":
                        print("Parabéns pela compra!")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    elif saldo <= "6999":
                        print("Voçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.")
                        voltar = "voltar"
        case "2":
            print("Pc 2")
            print("Processador: Ryzen 7 5700X")
            print("Placa de Vídeo: RTX 4060 ")
            print("Mémoria Ram: 16GB Ram")
            print("SSD: 512GB ")
            print("Placa mãe: B450 Aorus Elite")
            print("Fonte: 650W Corsair")
            print("Preço: R$4000,00")
            voltar = input("Digite: voltar, se quiser voltar. E se quiser Proseguir digite: comprar,  ")
            if voltar == "comprar":
                print(f"Voçe deseja comprar esse Pc? seu saldo é R${saldo}  ")
                comprar = input("[S/N]  ")
                if comprar == "sim" or comprar == "S" or comprar == "Sim":
                    if saldo >= "4000":
                        print("Parabéns pela compra!")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    elif saldo <= "3999":
                        print("Voçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.")
                        voltar = "voltar"
        case "3":
            print("Pc 3")
            print("Processador: Ryzen 5 5500")
            print("Placa de Vídeo: RTX 3050")
            print("Mémoria Ram: 16GB Ram")
            print("SSD: 1TB ")
            print("Placa mãe: B450 MSI Pro")
            print("Fonte: 550W Fsp")
            print("Preço: R$3000,00")
            voltar = input("Digite: voltar, se quiser voltar. E se quiser Proseguir digite: comprar,  ")
            if voltar == "comprar":
                print(f"Voçe deseja comprar esse Pc? seu saldo é R${saldo}  ")
                comprar = input("[S/N]  ")
                if comprar == "sim" or comprar == "S" or comprar == "Sim":
                    if saldo >= "3000":
                        print("Parabéns pela compra!")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    elif saldo <= "2999":
                        print("Voçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.")
                        voltar = "voltar"
        case "4":
            print("Pc 4")
            print("Processador: Ryzen 5 5600X")
            print("Placa de Vídeo: Rx 6600")
            print("Mémoria Ram: 16GB Ram")
            print("SSD: 1TB")
            print("Placa mãe: B450 Asus Tuf")
            print("Fonte: 650W Msi")
            print("Preço: R$3500,00")
            voltar = input("Digite: voltar, se quiser voltar. E se quiser Proseguir digite: comprar,  ")
            if voltar == "comprar":
                print(f"Voçe deseja comprar esse Pc? seu saldo é R${saldo}  ")
                comprar = input("[S/N]  ")
                if comprar == "sim" or comprar == "S" or comprar == "Sim":
                    if saldo >= "3500":
                        print("Parabéns pela compra!")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    elif saldo <= "3499":
                        print("Voçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.")
                        voltar = "voltar"
        case "5":
            print("Pc 5")
            print("Processador: Intel I5 12400F")
            print("Placa de Vídeo: RTX 2060")
            print("Mémoria Ram: 16GB Ram")
            print("SSD: 512GB")
            print("Placa mãe: B660M Dhs")
            print("Fonte: 600W Corsair")
            print("Preço: R$3200,00")
            voltar = input("Digite: voltar, se quiser voltar. E se quiser Proseguir digite: comprar,  ")
            if voltar == "comprar":
                print(f"Voçe deseja comprar esse Pc? seu saldo é R${saldo}  ")
                comprar = input("[S/N]  ")
                if comprar == "sim" or comprar == "S" or comprar == "Sim":
                    if saldo >= "3200":
                        print("Parabéns pela compra!")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    elif saldo <= "3199":
                        print("Voçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.")
                        voltar = "voltar"
                        