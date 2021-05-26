i=1
while i<=6:
    j=1
    while j<=6:
        if i+j==3 or j-i==3 or i-j==3 or i+j==9:
            print( "*", end= " " )
        else:
            print(" ",end=" " )
        j=j+1
    print() 
    i=i+1
    