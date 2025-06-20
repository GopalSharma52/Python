a=int(input("Enter a number:")) 
for i in range(a):
      # p=a-i
      for j in range(a-i):
            print(j+1,end="")
      for j in range(2*i):
            print("*",end="")
      for j in range(a-i,0,-1):
            print(j,end="")  
            # p=p-1     
      print()  
          