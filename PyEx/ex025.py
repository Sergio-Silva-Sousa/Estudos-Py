n = str(input('Digite um nome: ')).strip().split()
j = ' '.join(n)
r = 'silva' in j.lower()
r2 = str(r).replace('True', 'tem').replace('False', 'não tem')
print(f'No nome {j.title()} {r2} o sobrenome Silva.')
