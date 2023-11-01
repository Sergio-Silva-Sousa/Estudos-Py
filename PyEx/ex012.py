preco = float(input("Qual o preço do produto? R$"))
por= float(input("Quanto % de desconto você recebeu? "))
p = preco  - (preco * por / 100)
print(f'O seu produto com {por:.0f}% de desconto fica R${p:.2f}')