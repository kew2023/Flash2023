def p(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a1 = '228'
a2 = '777'
alf = '0123456789'
arr = []

for n in alf:
    
    a = int('228777'+ n)
    if p(a): arr.append(a)

    if n != 0:
        a = int(n + '228777')
        if p(a) and a <= 5000000: arr.append(a)

    a = int('22877'+n+'7')
    if p(a): arr.append(a)

    a = int('2287'+n+'77')
    if p(a): arr.append(a)
    
    a = int('228'+n+'777')
    if p(a): arr.append(a)

print(max(sorted(arr))+100000)
