from time import sleep 

print('\033[34;1mAnalizador de Média\033[m')
#Pegar informações básicas 
mn = str(input('\033[33;1mMédia mínima:\033[36;1m ').replace(',', '.'))
n1 = str(input("\033[33;1mDigite a primeira nota:\033[36;1m ").replace(',', '.'))
n2 = str(input('\033[33;1mDigite a segunda nota:\033[36;1m ').replace(',', '.'))
#Remover o ponto 
rfm = mn.replace('.', '')
rfn1 = n1.replace('.', '')
rfn2 = n2.replace('.', '')
#Contar os pontos
cm = mn.count('.')
cn1 = n1.count('.')
cn2 = n2.count('.')
#Verifica se tem mais de um ponto ou se começa ou termina.
if cm <= 1 and cn1 <= 1 and cn2 <= 1 and not mn.startswith('.') and  not mn.endswith('.') and not n1.startswith('.') and not n1.endswith('.') and not n2.startswith('.') and not n2.endswith('.'):
    if not (rfm.isdigit() and rfn1.isdigit() and rfn2.isdigit()):
        print("\033[31;1mERROR\033[33;1m (Você só pode digitar números)\033[m")
    else:
        #Transforma em Float
        mn = float(mn)
        n1 = float(n1)
        n2 = float(n2)
        #Cálculo
        me = (n1 + n2) / 2
        #Verifica a média 
        if me >= mn:
            print(f'\033[33;1mSua média foi \033[36;1m{me:2f}')
            sleep(1)
            print('\033[33;1mVocê foi ...\033[m')
            sleep(2)
            print('\033[32;1mAPROVADO\033[m')
        else:
            print(f'\033[33;1mSua média foi \033[36;1m{me:.2f}')
            sleep(1)
            print('\033[33;1mVocê foi ...\033[m')
            sleep(2)
            print('\033[31;1mREPROVADO\033[m')
else:
    #Erro
    print('\033[31;1mERROR\033[33;1m(Isso não é um número valido)\033[m')
    