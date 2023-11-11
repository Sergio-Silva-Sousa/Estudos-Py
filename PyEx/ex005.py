num = input('\033[34;1mDigite um número:\033[33;1m ')
if not num.isdigit():
    print('\033[31;1mERROR\033[33;1m(So posso identificar números inteiros)\033[m')
else:
    num = int(num)
    print(f'\033[36;1mSucessor:\033[32;1m {num + 1}')
    print(f'\033[36;1mAntecessor:\033[32;1m {num -1}\033[m')