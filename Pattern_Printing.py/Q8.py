a=int(input("Enter a number:"))
# for i in range(a,0,-1):
#               print("*"*i)
for i in range(a):
      for j in range(a-i):
            print("*",end="")
      print()      
5