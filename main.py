liczby=str(input())
n= int(liczby[0])
k= int(liczby[2])
s= n-k
def silnia_n(n):
    if n > 1:
        return n*silnia_n(n-1)
    return 1

def silnia_k(k):
    if k > 1:
        return k*silnia_k(k-1)
    return 1

def silnia_s(s):
    if s > 1:
        return s*silnia_s(s-1)
    return 1

wynik= silnia_n(n)/(silnia_k(k)*silnia_s(s))
print(int(wynik))