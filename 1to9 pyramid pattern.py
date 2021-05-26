# i=1
# k=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=k:
#         print(j,end=" ")
#         j=j+1
#     k=k+2
#     print()
#     i=i+1





i=1
k=65
while i<=5:
    b=1
    while b<=5-1:
        print(" ",end=" ")
        b=b+1
    j=i
    while j<=k:
        print(chr(j),end=" ")
        j=j+1
    k=k+1
    i=i+1
    print()