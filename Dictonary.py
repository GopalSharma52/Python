#Meri full bio data dictionary
Myinfo = {
      #key      # value        #values can be change but keys never
      "Name" : "Gopal Sharma",
      "Marks 10th class" : 86,
      "Father's name": "Mr. Shree Kant Sharma",
      "Mother's name" : "Mrs.Geeta devi",
      "Age" : 19,
      "Weight" : 61.5,
}
print(type(Myinfo))
print(Myinfo["Name"])
Myinfo["Height"]=5 ,"feet"
print(Myinfo)
Myinfo["Name"]="Shiva"#dictionary are mutable so changes are possible
print(Myinfo)
print(Myinfo.keys())#print all the keys 
print(Myinfo.values())#print all the values
print(Myinfo.items())#returns keys with values
print(Myinfo.get("Age"))
