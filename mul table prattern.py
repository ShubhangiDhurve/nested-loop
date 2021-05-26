# n=int(input("enter the number"))
# z=int(input("enter the number"))
# i=n
# while i<=z:
#         j=1
#         while j<10:
#                 print(i ,"*",j,"=",(i*j))
#                 j+=1
#         print()
#         i=i+1







a=int(input("enter the number"))
s=1
while s>0:
        num=a//100*100
        n1=a//10
        n2=n1%10
        n3=n2*10
        s=a%10
        s=s+1
        print(num,"+",n3,"+",s-1)
        break

# n=int(input("enter the number"))
# depth=1
# rem=n%1
# while rem<n:
#         s=depth*10
#         rem=n%10
#         rem=a%10
#         depth+=1

# a= int(input("enter the no."))
# i=1
# while i<=a:

# b=567//100*1000
# # c=b%10
# # d=c*10
# # print(b)
#         # =a//100*1000
# n1=1234//100
# n2=n1%1000
# n3=n2*1000
# print(n1)