n=5
a=1
b=n*2-1
i=1
while i<=n:
    j=1
    while j<n*2:
        if j==a or j==b:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    a=a+1
    b=b-1
    print()
    i=i+1