i=1
while i<=100:
    j=2
    count=0
    while j<i-1:
        if i%j==0:
            count=count+1
        j=j+1
    if i!=1 and count==0:
        print(i)
    i=i+1
    
# n=int(input("enter the number"))
# power=1
# while power<=n/2:
#     power=2*power
#     print(power)
#     sum=0
#     i=1
#     while i<=n:
#         sum+=i
#         print(sum)
#         num=1
#         num*=1
#         print(num)
#     i=i+1
# i=0
# while i<=n:
#     print(i+""+2*Math.PI*i/n)
#     i=i+1
#     rul=1
#     i=2
#     while i<=n:
#         rul=rul+ " " + i + " " +rul
#     print(rul)
# i=i+1




