s =  '>' + '3'*30 + '2'*20 + '4'*40

while '>2' in s or '>3' in s or '>4' in s:
    if '>2' in s:
        s = s.replace('>2', '33>',1)
    if '>3' in s:
        s = s.replace('>3', '4>',1)
    if '>4' in s:
        s = s.replace('>4', '2>',1)

print(sum(map(int,s[:-1])))
