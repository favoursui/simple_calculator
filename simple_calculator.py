# A simple calculator

print ('''1. Addition
2. Subtraction
3. Multiplication
4. Division
''')

print ("enter two numbers to add")

# accepts input from the user and stores it
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))

# sum up the inputs collected and convert to float
sum = float(first_number) + float(second_number)
print ("{} + {} = {:,.2f}" .format(first_number, second_number, sum))


print ("enter two numbers to subtract")
   
# accepts input from the user and stores it
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
 
# make a subtraction fom the inputs collected and convert to float
sub = float(first_number) - float(second_number)
print ("{} - {} = {:,.2f}" .format(first_number, second_number, sub))


print ("enter two numbers to multiply")
  
# accepts input from the user and stores it
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
  
# make a multiplication with the inputs collected and convert to float
mul = float(first_number) * float(second_number)
print ("{} * {} = {:,.2f}" .format(first_number, second_number, mul))


print ("enter two numbers to divide")
  
# accepts input from the user and stores it
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
  
# make a division with the inputs collected and convert to float
div = float(first_number) / float(second_number)
print ("{} / {} = {:,.2f}" .format(first_number, second_number, div))


print ("enter a number to exponent")
 
# accepts input from the user and stores it
first_number = int(input("enter first number: "))
exponent = int(input("enter exponent: "))
 
# make an exponential
expo = float(first_number) ** float(second_number)
print ("{} ** {} = {:,.2f}" .format(first_number, exponent, expo))


  
print ("enter two numbers to floor_divide")
 
# accepts input from the user and stores it
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
 
# make a floor_division with the inputs collected and convert to float
floor_div = float(first_number) // float(second_number)
print ("{} // {} = {:,.2f}" .format(first_number, second_number, floor_div)) 









