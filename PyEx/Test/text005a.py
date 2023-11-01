'''n = str(input('Digite seu nome: '))
if n == 'Sérgio':
    print('Seu nome é muito lindo!')
else:
    print('Seu nome é muito normal!')
print(f'Bom dia {n}!')'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segundo nota: '))
m = (n1 + n2) / 2
print(f'Sua média é {m:.1f}')
if m >= 6:
    print('Sua média é ótima!')
else:
    print('Sua média está péssima!')