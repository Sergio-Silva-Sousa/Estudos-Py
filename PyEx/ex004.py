n = input('\033[34;1mDigite algo:\033[33m ').strip()
ty = 'String'
v = '\033[32;1mVerdadeiro\033[m'
f = '\033[31;1mFalso\033[m'
r = f
c = n.count('.')
if not n.isalnum() and not n.isdigit():
    r = v
rf = n.replace('.', '')
if  rf.isdigit() and not n[-1] == '.' :
    ty = 'Inteiro'
    if '.' in n and not n[-1] == '.' and c == 1:
        ty = 'Float'
if n == 'True' or n == 'False':
    ty = 'Bool'
print(f"\033[1;32mO tipo primitivo desse valor é\033[1;35m {ty}\033[m")
print("\033[33;1mÉ um número?", str(rf.isnumeric()).replace('True', v).replace('False', f))
print('\033[33;1mÉ alfabético?', str(n.isalpha()).replace('True', v).replace('False', f))
print('\033[33;1mE alfanumérico?', str(rf.isalnum()).replace('True', v).replace('False', f))
print('\033[33;1mContém caracteres especial?', r)
print("\033[33;1mContém apenas espaços?", str(n.isspace()).replace('True', v).replace('False', f))
print('\033[33;1mContém apenas dígitos?', str(rf.isdigit()).replace('True', v).replace('False', f))
print('\033[33;1mEsta em minúscula?', str(n.islower()).replace('True', v).replace('False', f))
print('\033[33;1mEsta em maiúscula?', str(n.isupper()).replace('True', v).replace('False', f))