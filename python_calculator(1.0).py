
#Defines basic_caluculation as the function for addition, subtraction, multiplication, and division

def basic_calculation(num1, opperation, num2):
    if opperation == "+":
        sum = num1 + num2 
        print(sum)
    elif opperation == "-":
        diffrence = num1 - num2
        print(diffrence)
    elif opperation == "*":
        product = num1 * num2
        print(product)
    elif opperation == "/":
        quotient = num1 / num2
    else:
        print("Invalid opperation. Please enter "+" for addition, "-" for subtraction, "*" for multiplication or "/" for division.")


#Defines a list to be used to average numbers and the "basic_average" function to average numbers  
average_list = []
def basic_average():
    sum = 0
    for i in range(0,len(average_list)):
         sum = sum + average_list[i]
         average = sum / len(average_list)
    print(average)

#Asks the user what type of math they'd like to do 
user_math_choice = input("What type of math would you like to do? (i.e 'basic arithmatic', 'sin', 'percentage')")

#if statements used to call functions based on what the user requested in "user_math_choice"
if user_math_choice == "basic":
    basic_calculation(int(input("input your first number")), input("input your opperation (i.e '+')"), int(input("input your second number")))
elif user_math_choice == "average":
    num_of_nums =  int(input("How many numbers would you like to average?"))
    for i in range(num_of_nums):
        average_list.append(int(input("enter a number")))
    basic_average()

