s = '0123456789ABCDE'
ch = '02468ACE'
c = 0
'''
a1,a2,a3,a4 - составляющие числа, a1 != 0
Сколько существует четырехзначных чисел в пятнадцатиричной системе счисления, в которых одинаковые цифры не стоят рядом, а само число четное.
'''
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                if a1 != a2 and a2 != a3 \
                and a3 != a4 and a1 != '0':
                    c += 1
print(c)
