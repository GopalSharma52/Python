a=int(input("Enter a number:"))
for i in range(a+1):
      ch=65
      for j in range(i):
            print(chr(ch),end="")#chr ASCII value ko character me convert kar rha h
            ch+=1
      print()      