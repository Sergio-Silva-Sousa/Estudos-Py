f = str(input("Fala uma frase: ")).strip().lower()
p = f.count('a')
fp = f.find('a') + 1
fu= f.rfind('a') + 1
print(f'A letra A aparece {p} vezes \n Sua primeira aparição no índice {fp} e sua última aparição é no índice {fu}.')