print('\033[1;35m-=-' * 5 + "Calculadora" + '-=-'*5)
print("\033[1;33mAs funções da Calculadora são soma, multiplicar, subtrair e dividir. \033[m")
print('\033[1mPara escolher você só precisa digitar a primeira letra')
es = str(input('Escolha, por favor: ')).lower().strip()

if es != 'a' and es != 's' and es != 'd' and es != 'm':
    print('\033[1;36mMenu de Ajuda')
    print('\033[33m a: Adição \n s: Subtração \n d: Divisão \n m: Multiplicação \033[m')
else:
    n1 = input('n1: ').replace(',', '.')
    n2 = input('n2: ').replace(',', '.')
    if not (n1.replace('.', '', 1).isdigit() and  n2.replace('.', '', 1).isdigit()):
        print("\033[1;31m ERROR \033[33;1m(Você so pode digitar números) \033[m")
    else:
        n1 = float(n1)
        n2 = float(n2)

        if es == 'a':
            print(f'\033[1m{n1} + {n2} =', n1 + n2)
        if es == 's':
            print(f'm{n1} - {n2} =', n1 - n2)
        if es == 'd':
            if n2 == 0:
                print('\033[1;31mERROR\033[33m(Não é possível dividir por zero\033[m)')
            else:
                    print(f'{n1} ÷ {n2} =', n1 / n2)
        if es == 'm':
            print(f'{n1} x {n2} =', n1 * n2)