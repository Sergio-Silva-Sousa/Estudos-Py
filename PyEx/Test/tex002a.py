n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s}, o produto é {m} e a  divisão é {d:.3f}', end=', ')
print(f'Divisão inteira {di} e potência {e}')