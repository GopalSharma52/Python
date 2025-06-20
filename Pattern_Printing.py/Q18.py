a=int(input("Enter a number: "))
for i in range(a):
      ch=65
      for j in range(a-i):
            print(chr(ch),end="")
            ch+=1
      for k in range(i):
            print("  ",end="") 
      for j in range(a-i):
            print(chr(ch-1),end="")
            ch-=1          
      print()      