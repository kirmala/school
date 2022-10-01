p=int(input('P='))
Np=int(input(f'N{p}='))
N10=0
k=1
while(Np!=0):
    N10=N10+(Np % 10)*k

    k=k*p
    Np=Np//10
print(f'N10={N10}')
