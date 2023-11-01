n = int(input('Digite um número: '))
nu = n % 10
nd = n // 10 % 10
nc = n // 100 % 10
nm = n // 1000 % 10
print(f'Seu número tem: \n {nu} unidades \n {nd} dezenas \n {nc} centenas \n {nm} milhar')