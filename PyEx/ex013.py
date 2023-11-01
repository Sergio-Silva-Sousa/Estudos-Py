slr= float(input('Qual o salário atual do seu funcionário? R$'))
por = float(input('Quanto % você que aumentar do salário atual? '))
aum = slr + (slr * por  / 100)
print(f'O funcionário que ganhava R${slr:.2f}, com {por:.0f}% de aumento, passa a receber R${aum:.2f}')