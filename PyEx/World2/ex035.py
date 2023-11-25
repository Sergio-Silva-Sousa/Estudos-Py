n = int(input('Digite um número inteiro: '))
print('Base de conversão: \n 1-Binario \n 2-Octal \n 3-hexadécimal')
es = int(input('Escolha: '))
if es == 1:
      n = bin(n)
      print(n[2:])
elif es == 2:
       n = oct(n)
       print(f'Octal: {n[2:]}')
elif es == 3:
      n = hex(n)
      print(f'Hexadecimal: {n[2:]} ')
else:
      print('Escolha somente um dos números da tabela acima.l')
