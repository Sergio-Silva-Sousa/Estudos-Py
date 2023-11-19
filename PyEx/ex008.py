print('\033[1;35mConversor de metros\033[m')
m = str(input("\033[33;1mDigite uma distancia em metros: \033[36;1m")).replace(',', '.')

# Verificação
if m.replace('.', '') == '0':
    print('\033[31;1mERROR\033[33;1m(Não tem como existir 0 metros)\033[m')
else:
    if m.replace('.', '', 1).isdigit() and not m.startswith('.') and not m.endswith('.'):
        m = float(m)
        mm =  m * 1000
        cm = m * 100
        km = m / 1000
        In = m * 39.37
        ft = m * 3.280
        yd = m * 1.094
        mi = m / 1609.34
        nm = m / 1852
        mil = m * 39.37 * 1000
        print(f'\033[33;1mMilimetros: \033[36;1m{mm}')
        print(f'\033[33;1mCentímetros: \033[36;1m{cm}')
        print(f'\033[33;1mQuilômetros: \033[36;1m{km}' )
        print(f'\033[33;1mPolegadas:\033[36;1m {In}' )
        print(f'\033[33;1mPés: \033[36;1m{ft}')
        print(f'\033[33;1mJardas:\033[36;1m {yd}')
        print(f'\033[33;1mMilhas:\033[36;1m{mi} ')
        print(f'\033[33;1mMilhas Náuticas:\033[36;1m {nm}')
        print(f'\033[33;1mMils:\033[36;1m {mil}\033[m')
    else:
        print('\033[31;1mERROR\033[33;1m(Você não digitou um número válido)\033[m')