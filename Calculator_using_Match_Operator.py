a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))
operator=input("Enter a operator:")

match operator:
     case "+":
          print("The sum of entered number is:",a+b)
     case "-":
          print("The diff of entered number is:",a-b)     
     case "*":
          print("The product of entered number is:",a * b)
     case "/":
          print("The division of entered number is:",a/b)
     case "_":
          print("Enter a valid operator")