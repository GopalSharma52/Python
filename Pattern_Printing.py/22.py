# a=int(input("Enter a number: "))
# b=int(input("Enter second number: "))      #Is process ki help se ham a and b ko alag alag line me print karenge
n1=input("Enter two numbers: ")
n1=n1.split()
a=int(n1[0])#But is process ki help se a and b ko same line me print kar sakte hai space dekar Is processs me hamne sabse pahle list banayi or fir use split kar liya and the then data type int me convert kar diya
b=int(n1[1])
# print(type(a))
# print(type(b))
if(b>a):
 for i in range(a,b+1,1):
       if(i%2==0):
            print(i,end=" ")
 print()
elif(b<a):
 for i in range(a,b+1,-1):
       if(i%2==0):
            print(i,end=" ")
 print()           