#Program to make a simple calculator

#This function adds two numbers
def add(x, y):
    return x + y

#This function subtracts two numbers
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("*"* 50)
print("Select your Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("*"* 50)
print("\n")

while True:
    #take input from the user
    print("*" * 50)
    choice = input("Enter your choice(1/2/3/4): ")

    #chack if choice is one of the four options
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, " + ", num2, " = ", add(num1, num2))
        elif choice == '2':
            print(num1, " - ", num2, " = ", subtract(num1, num2))
        elif choice == '3':
            print(num1, " x ", num2, " = ", multiply(num1, num2))
        elif choice == '4':
            print(num1, " / ", num2, " = ", divide(num1, num2))

        #check if user wnats another calculatoion
        #break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")