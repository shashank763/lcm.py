a=int(input())
b=int(input())
if a>b:
    a,b=b,a
    c=b
    while True:
        if c%a==0 and c%b==0:
            print(b)
            break
        c+=1
