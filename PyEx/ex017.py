import math
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
h = math.sqrt((co**2) + (ca**2))
print(f'A hipotenusa vai medir {h:.2f}')