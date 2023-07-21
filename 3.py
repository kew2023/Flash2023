s = 'БУКВА'
k = 0 #Счетчик
dic = {'Б':0,'У':0,'К':0,'В':0,'А':0}
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    k += 1
                    if k >= 1200 and k <= 1500:
                        dic[a1] += 1
                        dic[a2] += 1
                        dic[a3] += 1
                        dic[a4] += 1
                        dic[a5] += 1
                    if k > 1500:
                        break

print(dic)
