d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados?'))
ttl = (d * 60) + (k * 0.15)
print(f'O total a pagar é R${ttl:.2f}')