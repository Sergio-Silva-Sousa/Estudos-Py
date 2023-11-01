import random 
a1 = str(input('1°: '))
a2 = str(input('2°: '))
a3 = str(input('3°: '))
a4 =  str(input('4°: '))
s = [a1, a2, a3, a4]
random.shuffle(s)
print(f'A ordem de apresentação de trabalho será: \n {s}')