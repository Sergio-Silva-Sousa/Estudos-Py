from time import sleep 
print('\033[34;1mAnalizador de Média\033[m')
mn = str(input('\033[33;1mMédia mínima:\033[36;1m ').replace(',', '.'))
n1 = str(input("\033[33;1mDigite a primeira nota:\033[36;1m ").replace(',', '.'))
n2 = str(input('\033[33;1mDigite a segunda nota:0\033[36;1m ').replace(',', '.'))
rfm = mn.replace('.', '')
rfn1 = n1.replace('.', '')
rfn2 = n2.replace('.', '')
if not (rfm.isdigit() and rfn1.isdigit() and rfn2.isdigit()):
    print("\033[31;1mERROR\033[33;1m(Você so pode digitar números)\033[m")
else:
    mn = float(mn)
    n1 = float(n1)
    n2 = float(n2)
    me = (n1+n2) / 2
if me >= mn:
    print(f'\033[33;1mSua média foi \033[36;1m{me:.2f}')
    sleep(1)
    print('\033[33;1mVocê foi ...\033[m')
    sleep(2)
    print('\033[32;1mAPROVADO\033[m')
else:
    print(f'\033[33;1mSua média foi \033[36;1m{me:.f}')
    sleep(1)
    print('\033[33;1mVocê foi ...\033[m')
    sleep(2)
    print('\033[31;1mREPROVADO\033[m')

    