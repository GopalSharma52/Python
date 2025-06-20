a=int(input("Enter a number: "))

for i in range(a):
      for j in range(a-i):
            print("  ",end="")
      n=1
      for k in range(i+1):
            print(int(n)," ",end="")
            n=n*(i-k)/(k+1)
      print()            