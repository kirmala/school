from math import log2


def info():
    var_to_find = input('что не известно? ')
    if var_to_find.lower().strip() == 'N':
        i = int(input('enter i '))
        print(2 ** i)
    elif var_to_find == 'i':
        what_to_use = input('what do you want to use(N then 1 | I,K then 2)')
        if what_to_use == 1:
            N = int(input())
            print(log2(N))
        elif what_to_use == 2:
            K, I = map(int, input().split())
            print(f'i={I / K}')
    elif var_to_find == 'I':
        what_to_use = input('what do you want to use(N,K then 1 | i,K then 2)')
        if what_to_use == '1':
            N, K = map(int, input().split())
            i = log2(N)
            print(f'I={K * i}')
        else:
            K, i = map(int, input().split())
            print(f'I={K * i}')
    elif var_to_find == 'K':
        what_to_use = input('what do you want to use(N,I then 1 | i,I then 2)')
        if what_to_use == 1:
            N, I = map(int, input().split())
            i = log2(N)
            print(f'I={I / i}')
        else:
            I, i = map(int, input().split())
            print(f'K={I / i}')


def image():
    var_to_find = input('что не известно?')
    if var_to_find == 'K':
        b = int(input('enter b'))
        print(f'k = {2 ** b}')
    elif var_to_find == 'b':
        K = int(input('enter K'))
        print(f'b = {log2(K)}')


def sound():
    var_to_find = input('что не известно?')
    if var_to_find == 'H':
        t = int(input('enter t'))
        print(f'H = {1 / t}')
    elif var_to_find == 't':
        H = int(input('enter H'))
        print(f't = {1 / H}')


def f11():
    type_of_data = input("c каким типом данным хотите работать?(изображение\звук\информация)")
    if type_of_data.lower().strip() == "изображение":
        image()
    elif type_of_data.lower().strip() == "звук":
        sound()
    elif type_of_data.lower().strip() == "информация":
        info()


if __name__ == '__main__':
    f11()
