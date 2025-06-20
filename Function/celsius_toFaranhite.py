def tem_c_to_f(Celsius):
      faranhiet=(Celsius*9/5)+32
      return(faranhiet)
a=int(input("Enter temp in celsius:"))
c=tem_c_to_f(a)
print("The temp in faranheit: ",c)