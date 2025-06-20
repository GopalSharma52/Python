n=int(input("Enter a number:"))
k=n
sum=0
rev=0
while(n>0):
   d=n%10
   n=n//10#double divide ka mtlb hota h bina point ke ans aana OR single divide se decimal me aata h
   sum=sum+d
   rev=(rev*10+d)
print(sum)
print(rev)
if(rev==k):
 print("numer is pallindrom")
else:
 print("Number is not pallindrome")
 

