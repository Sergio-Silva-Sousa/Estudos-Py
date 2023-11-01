s = float(input('Qual o salário do seu funcionário? R$'))
if s <= 1250:
    am = s + (s * 15 / 100)
else:
    am = s + (s * 10 / 100)
print(f'O funcionário que ganhava {s:.2f}, com o aumento passa a receber R${am:.2f}')