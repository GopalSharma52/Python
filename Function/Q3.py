def airthmatic (a,b):
      c=a+b
      d=a-b
      e=a*b
      f=a/b
      return c,d,e,f
a=int(input("ENter a number: "))
b=int(input("ENter second number: "))
m,n,o,p=airthmatic(a,b)
# print("Sum,diff,Mul,div:",result)
# print("sum of the given numbers is: ",result[0])
# print("diff of the given numbers is: ",result[1])
# print("Mult of the given numbers is: ",result[2])
# print("div of the given numbers is: ",result[3])
print("sum of the given numbers is: ",m)
print("diff of the given numbers is: ",n)
print("Mult of the given numbers is: ",o)
print("div of the given numbers is: ",p)