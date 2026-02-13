import sys
import os
from time import sleep

voltar = "voltar"
comprar = "comprar"
print("Deseja entrar na loja de PC's? ")
entrar = input("[S/N]  ").strip().lower()
if entrar in ["s", "sim"]:
    print("\033[1mVoçe entrou na loja de Pc's!\033[0ms")
    print("\033[1mAgora voçe pode escolher algum Pc\033[0ms")
else:
    sys.exit(print("Voçe foi embora "))

saldo = float(input("Digite qual seu saldo R$"))

print(f"Seu saldo agora é R${saldo}")

while voltar == "voltar":
    print("Qual voçe deseja escolher? Escolha e veja as configs!")

    op = input("  1/2/3/4/5 ou caso queira sair digite: sair  ").strip().lower()
    if op == "sair" or op == 's':
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
            voltar = input("Digite: voltar, se quiser voltar. E se quiser Proseguir digite: comprar,  ").strip().lower()
            if voltar in ["comprar", 'compra']:
                print(f"Voçe deseja comprar esse Pc? seu saldo é R${saldo}  ")
                comprar = input("Digite [S/N] ").strip().lower()
                if comprar in ["s", "sim"]:
                    if saldo >= 7000:
                        print("\033[1;32mParabéns pela compra!\033[m")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    else:
                        print("\033[1;31mVoçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.\033[m")
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
                comprar = input("Digite [S/N] ").strip().lower()
                if comprar in ['s', 'sim']:
                    if saldo >= 4000:
                        print("\033[1;32mParabéns pela compra!\033[m")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    else:
                        print("\033[1;31mVoçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.\033[m")
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
                comprar = input("Digite [S/N] ").strip().lower()
                if comprar in ['s', 'sim']:
                    if saldo >= 3000:
                        print("\033[1;32mParabéns pela compra!\033[m")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    else:
                        print("\033[1;31mVoçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.\033[m")
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
                comprar = input("Digite [S/N] ").strip().lower()
                if comprar in ['s', 'sim']:
                    if saldo >= 3500:
                        print("\033[1;32mParabéns pela compra!\033[m")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    else:
                        print("\033[1;31mVoçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.\033[m")
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
                comprar = input("Digite [S/N] ").strip().lower()
                if comprar in ['s', 'sim']:
                    if saldo >= 3200:
                        print("\033[1;32mParabéns pela compra!\033[m")
                        sys.exit(print("Obrigado por visitar nossa loja!"))
                    else:
                        print("\033[1;31mVoçe não tem o saldo suficiente. Escolha um Pc de acordo com seu orçamento.\033[m")
                        voltar = "voltar"
