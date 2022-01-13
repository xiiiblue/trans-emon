s = 'abcde'
for c in s:
    print(c)
    if c == 'b':
        s=s.replace('b','')

print(s)