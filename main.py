import math
liczby=str(input().split(" "))
n= int(liczby[0])
k= int(liczby[2])

if k == 1 or k == n:
    print(1)

if k > n:
    print(0)
else:
    silnia_n= math.factorial(n)
    silnia_k= math.factorial(k)
    dwumian= silnia_n // (silnia_k*(n-k))
    print(dwumian)