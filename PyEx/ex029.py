v = int(input('Em quanto km/h você estava andando? '))
if v > 80:
    m = float((v - 80) * 7)
    print(f'Você foi multado em R${m:.2f}, por ultrapassar limite de velocidade de 80km/h.')
print('Dirija com segurança!')