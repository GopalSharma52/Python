a=int(input("Enter a number:"))
count=1
for i in range(a):
      for j in range(i+1):
            print(count,end=" ")
            count+=1
      print()      