def dell(x,a):
    return x % a == 0

for a in range(1,200):
    for x in range(1,1000):
        f = ((not dell(72,x)) or (not dell(120,x))) or (a-x > 100)
        if f == 0:
            break
    else:
        print(a)
        break
