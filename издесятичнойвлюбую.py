N10=int(input('N10='))
p=int(input('p='))
k=1
Np=0

while(N10!=0):
    Np=Np+(N10%p)*k
    k=k*10
    N10=N10 // p
print(f'N{p}={Np}')
