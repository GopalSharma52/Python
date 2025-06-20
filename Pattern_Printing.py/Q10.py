a=int(input("Enter a number:"))
for i in range(1,a+1):
      for j in range(1,2*i):
            if((i+j)%2==0):
                  print("A",end=" ")
            else:
                  print("B",end=" ")    
      print()     
      