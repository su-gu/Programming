a = int(input("Enter a number"))
for i in range(1, a+1):
    print((i*2)-1, end='')
    if i != a:
        print(', ',end='')
    
    