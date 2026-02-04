modo = input('Qual temperatura voçe deseja converter? \n [1] De Celsius > Fahreheit \n [2] De Fahreheit > Celsius \n  ')

if modo == '1':
    celsius = float(input('Informe a tempera em °C:  '))
    fahreheit = ((9 * celsius) / 5) + 32
    print(f'A temperatura de corresponde a {fahreheit}°F!')

elif modo == '2':
    fahreheit = float(input('Informe a tempera em °F:  '))
    celsius= ((9 * fahreheit) / 5) + 32
    print(f'A temperatura de corresponde a {celsius}°C!')