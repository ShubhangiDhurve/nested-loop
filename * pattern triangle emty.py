row=int(input("enter the rows"))
i=1
while i<=row:
    j=1
    while j<=i:
        if j==1 or j==i or i==row:
             print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1





























