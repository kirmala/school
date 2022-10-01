p=int(input('введите систему счисления'))

for x in range(1,p):
    for y in range(1,p):
        z=(x*y // p)*10 + (x*y) % p
        print(z,end='')
    print()
