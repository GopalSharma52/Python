a=int(input("Enter a number: "))
for i in range(a):
      for j in range(a-i):
            print("*",end="")
      for k in range(i):
            print("  ",end="")
      for j in range(a-i):
            print("*",end="")            
      print()      