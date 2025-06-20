a=int(input("Enter a number: "))
c=int(input("Enter another number: "))
b=0
sum=0
for i in range(a):
     d=b*10+c
     b=d
     sum+=d
     print(d,end="+")
print("=",sum,end="")
print()     
