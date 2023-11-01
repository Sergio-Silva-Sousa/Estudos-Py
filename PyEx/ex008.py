m = float(input("Digite uma distancia em metros: "))
mm= m * 1000
c = m * 100
hm = m / 100
dm = m * 10
dam = m / 10
km = m / 1000
print(f'{m} metros convertido para:\n Centímetros: {c:.0f} \n Milímetros: {mm:.0f} \n Hectometro: {hm} \n Decímetro: {dm:.0f} \n Decametro: {dam} \n Quilômetros: {km}')