from random import randint
import emoji
from time import sleep
ns= randint(0, 5)
print('-=-' * 17)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!!!')
print('-=-' * 17)
j = int(input('Em que número eu pensei: '))
print('PROCESSANDO....')
sleep(2)
if ns == j:
    print('Parabéns, Você me Venceu😥')
else:
    print(f'Você ERROU!!!. Eu pensei no número {ns}.')