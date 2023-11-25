an = int(input('Informe sua data de nascimento: '))
mn = 2023 - an
if mn < 18:
      print(f'Você ainda não pode se alistar, falta {18-mn} anos.')
elif mn > 18:
      print(f"Você está atrasado, deveria ter se alistado há {mn-18} anos atrás.")
else:
      print('Você esta na idade de se alistar!')