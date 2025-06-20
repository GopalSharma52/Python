b=int(input("Enter cost price:"))
a=int(input("Enter selling price:"))
if(a>b):
      print("seller got profit of:")
      print(a-b,"Rupees")
      print((a-b)/a*100,"%")
else:
      print("Seller got loss of:")
      print(b-a,"Rupees")    
      print((a-b)/b*100,"%")