vlr_cs = float(input('Qual o valor da casa? '))
slr = float(input('Quanto você recebe? '))
ans = int(input('Em quantos anos você irá pagar?')) * 12
p = (slr * 30) / 100
pr_ms = vlr_cs / ans
if pr_ms > p:
    print('Você iria fica um pouco apertado,  assim inprestimo negado')
else:
    print(f'Você ira pagar R${pr_ms:.2f} mensalmente, por {ans} meses. ')

