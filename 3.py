from functools import lru_cache

def m(s):
    a,b = s
    return (a*4,b),(a,b*4),(a+1,b),(a,b+1)

@lru_cache(None)
def g(s):
    if sum(s) >= 105: return 'W'
    if any(g(snew) == 'W' for  snew in m(s)): return 'P1'
    if all(g(snew) == 'P1' for snew in m(s)): return 'B1' #Для 19-ого заменить на any
    if any(g(snew) == 'B1' for snew in m(s)): return 'P2'
    if all(g(snew) == 'P2' or  g(snew) == 'P1' for snew in m(s)): return 'B2/1'

for s in range(1,100+1):
    k = (4,s)
    print(g(k),s)
