char=(input("enter the char"))
j=0
while j<len(char):
    print(char.upper()[j]+char.lower()[j]*(j),end=" ")
    if j!=len(char):
        print("_",end=" ")
    j=j+1

    

                




# char=(input("enter the number"))
# i=len(char)-1
# while i>=0:
#     print(char.upper()[i]+char.lower()[i]*(i),end=" ")
#     if i!=len(char):
#         print("_",end=" ")
#     i=i-1
