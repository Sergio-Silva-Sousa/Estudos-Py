n1 = float(input("Primeira nota: "))
n2 = float(input('Segunda nota: '))
m = (n1+n2) / 2
if m < 5:
      print(f'Sua média foi {m}, você foi reprovado')
elif m >= 5 and m <= 6.9:
            print(f'Sua média foi {m}, você está de recuperação ')
else:
      print(f'Sua média foi {m}, você foi aprovado!!')