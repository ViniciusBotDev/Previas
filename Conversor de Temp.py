import os

continuar = "s"

while continuar == "s" or continuar == "S":
    os.system('cls')

    print("---Conversor de Temperatura---")

    celsius = float(input("Qual a temperatura em graus celsius: "))

    farenheit = (celsius * 1.8) + 32

    print(f"{celsius}°C equivale a {farenheit}°F")

    if farenheit >= 90:
        print("Está muito quente")
    else :
        print("A temperatura está boa")
    continuar = input("Quer continuar?  ")

print("Fim!")