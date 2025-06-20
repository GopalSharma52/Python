Marks=[23,34,45,56,56,67,89,]
print(Marks[3])
#Marks[6]="Kanhaiya"
print(Marks)
print(len(Marks))
#Marks[0]="shiva"#lists are mutable so changes allowed
#slicing
print(Marks[1:4])# Aakhri wala indexing ka number count nhi hota isliye output 1 se 3 tak ki indexing ka aayega
print(Marks[0:4])# indexing list ki 0 se start hoti h 
print(Marks[:4])# Agr index ka pahla number nhi diya to automatically zero indexing se le lega
print(Marks[1:0])
print(Marks[1:])# Agar aakhari indexing number nhi diya to automatically last indexing tak asssume kar lega
#Negative me indexing pichhe se hoti hai or -1 se start hoti h
print(Marks[-3:-1])      
#print(Marks.append("Ankit"))#(Exeptional case) agar ise ham print karayenge to print nhi hoga.
print(Marks.remove(34))#this is a method so this will not print
print(Marks)
(Marks.sort())
Marks.reverse()#puri list ko rev karta h
Marks.insert(0,90)#(#index,want to insert element)
Marks.pop(3)
print(Marks)
