a = int(input())
a = a-1 if a%2 ==0 else a
for i in range(1, a+1):
    print((i*2)-1, end='')
    if i != a:
        print(', ',end='')