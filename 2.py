a = int(input())
for i in range(1,a+1):
    if i % 2 == 0 or i%5 == 0:
        series = range(i, 0, -1)
    else: 
        series = range(1,i+1)
    for j in series:
        print(j, end= '')
        if i!=1  and j!=series[-1]:
            print('*',end='')
    print()
