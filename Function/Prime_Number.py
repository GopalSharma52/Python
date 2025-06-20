def prime(a):
      flag=0
      for i in range(2,a,1):
            if(a%i==0):
                  print("Above number is not prime")
                  flag = 1
                  break
      if(flag==0):
       print("prime")
prime(0)                      