n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
m = n1
mn = n1
if n2 > m:
    m = n2
if n3 > m:
    m = n3
if n2 < mn:
    mn = n2
if n3 < mn:
    mn = n3
print(f'O maior número entre {n1}, {n2} e{n3} é {m}, ja o menor é {mn}.')