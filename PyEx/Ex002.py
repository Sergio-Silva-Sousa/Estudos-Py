n = input('\033[1;35mDigite seu nome:\033[m ')
v1 = False
if n == '':
    v1 = True
if n.isnumeric() or n.isspace()  or  v1  == True:
    print('\033[1;31m ERROR \033[m \033[33;1m(Você não pode deixar em branco, e também não pode conter só números!) \033[m')
else:
    print(f'\033[1;36mSeja muito bem vindo ao meu sistema\033[m,\033[32;1m{n}\033[m!')