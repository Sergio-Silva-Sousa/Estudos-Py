real = float(input('Quantos reais você tem? '))
dolar = real / 5.03
iene = real * 29.77
euro = real / 5.34
print(f'Com R${real} você pode comprar: \n USD : {dolar:.2f} \n EUR : {euro:.2f} \n JPY: {iene:.2f}')