ss = input().split(' ')
a, b, c, n = map(int, ss)

if n < 3  or  not(a>0 and b>0 and c>0)  or  a+b+c < n:
    print('NO')
else:
    print('YES')