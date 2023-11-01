a = float(input('Valor da primeira reta: '))
b = float(input('Valor da segunda reta: '))
c = float(input('Valor da terceira reta: '))
if (a+b > c) and (a+c > b) and (b + c > a):
    print(f'Os lados {a:.1f}, {b:.1f} e {c:.1f}, criam um triângulo valido.')
else:
    print(f'Os lados {a:.1f}, {b:.1f} e {c:.1f} não formam um triângulo ')
