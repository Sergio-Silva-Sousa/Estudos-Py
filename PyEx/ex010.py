print('\033[33;1mConversor')
real = str(input('\033[37;1mQuantos reais você tem?\033[32;1m ')).replace(',', '.').strip()
if real.replace('.', '', 1).isdigit() and not real.startswith('.') and not real.endswith('.')  and not real == '0':
    real = float(real)
    dolar = real * 0.20600
    iene = real * 30.398
    euro = real * 0.18820
    ps_arg = real * 72.8827
    ps_mex = real * 3.52099
    lb_es = real  * 0.16203508
    ru_in = real * 17.022234
    dolar_aus = real * 0.31047742
    yuan = real * 1.4564377 
    frc_ru = real * 252.88354
    print(f'\033[37;1mDolar:\033[32;1m {dolar:.2f}')
    print(f'\033[37;1mIene:\033[32;1m {iene:.2f}')
    print(f'\033[37;1mEuro:\033[32;1m {euro:.2f}')
    print(f'\033[37;1mPeso Argentina:\033[32;1m {ps_arg:.2f}')
    print(f'\033[37;1mPeso Méxicano:\033[32;1m {ps_mex:.2f}')
    print(f'\033[37;1mLibra esterlinar:\033[32;1m {lb_es:.2f}')
    print(f'\033[37;1mRúpia Indiana:\033[32;1m {ru_in:.2f}')
    print(f'\033[37;1mDolar Austráliano:\033[32;1m {dolar_aus:.2f}')
    print(f'\033[37;1mYuan:\033[32;1m {yuan:.2f}')
    print(f'\033[37;1mRwandan Francs:\033[32;1m {frc_ru:.2f}', '\033[m')
else:
    print('\033[31;1m Digite um valor válido\033[m')