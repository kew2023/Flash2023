#НИКТО
s = 'АГРОТЕХНИК'
k = 0 #Счетчик
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    k += 1
                    if a1+a2+a3+a4+a5 == 'НИКТО':
                        print(k)
                        break
