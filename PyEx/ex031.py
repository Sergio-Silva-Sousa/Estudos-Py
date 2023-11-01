d = int(input('Qual é a distância da sua viagem? '))
p = d * 0.50 if d <= 200 else d * 0.45
print(f'Você está prestes a começar uma viagem de {d}Km. \n Sua passagem custará R${p:.2f}.')