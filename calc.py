#This is a bsic calculator, which can perform 4 Arithmetic Operations, Add, Subtract, Multiply and Divide.
#Note: It Does Not loop.

print(''' __     __        _ _     _           _   
 \ \   / /       | | |   (_)         | |  
  \ \_/ /   _  __| | |__  _  ___  ___| |_ 
   \   / | | |/ _` | '_ \| |/ _ \/ _ \ __|
    | || |_| | (_| | | | | |  __/  __/ |_ 
    |_| \__,_|\__,_|_| |_| |\___|\___|\__|
                        _/ |              
                       |__/               \n \n  Be Sure to check out more of my work on my GitHub Profile, https://github.com/Yudhjeet \n''')

num1= int(input("Enter First number:"))
num2= int(input("Enter Second number:"))

ch= (input('''Choose one of the following 
             + for addition \n
             - for subtraction \n
             * for multiplication \n
             / for divison \n
             >>>>''')) #Takes the input

sum= num1+num2
difference= num1-num2
product= num1*num2
quotient= num1/num2

if ch == '+': #Condition to check the input of ch, if +, print sum variable.
    print("Sum:", sum)
elif ch == '-': #Condition to check the input of ch, if -, print difference variable.
    print("Difference:", difference)
elif ch == '*': #Condition to check the input of ch, if *, print product variable.
    print("Product:", product)
elif ch == '/': #Condition to check the input of ch, if /, print quotient variable.
    print("Quotient:", quotient) 
else: #Condition to check the input, if none of the options given, it prints :Incorrect Operator"..
    print("Incorrect Operator")

