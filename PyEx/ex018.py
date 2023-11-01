import math
ang = float(input ('Digite um ângulo qualquer: '))
angr = math.radians(ang)
sin = math.sin(angr)
cos = math.cos(angr)
tan = math.tan(angr)
print(f'O ângulo de  {ang} tem o SENO de {sin:.2f} ')
print(f'O ângulo de {ang} tem o COSSENO de {cos:.2f}')
print(f'O ângulo {ang} tem o TANGENTE de {tan:.2f}')