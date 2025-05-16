import re
number_pattern = r"^\d+\.\d+|\-\d+\.\d+|\d+|\-\d+$" #accepts both negative and positive numbers(intigers and decimals)

def add(x,y):    
    return x+y
def subtract(x,y):  
    return x-y
def multiply(x,y):  
    return x*y
def divide(x,y):  
    if y==0:
        print("Unable to divide by 0")
        exit()
    else:
        return x/y
        
def num_input(id):
    number=0
    unverified_number =input(f"Enter the {id} number: ")
    if re.match(number_pattern,unverified_number):
        number=float(unverified_number)        
    else:
        print("Invalid number, try again!")
        number=num_input(id)
    return number    

def show_menu():
    print("\nSelect your operation")
    print("1. Addition.")
    print("2. Substraction.")
    print("3. Multiplication.")
    print("4. Division.")
    print("5. Exit.")
    operation = int(input("Type your choice: "))
    return operation

def userPrompt():
    num1=num_input("first")
    num2=num_input("second")
    print(f"\nFirst Number: {num1} \nSecond Number: {num2}")
    return (num1,num2)

def main():
    print("--------start-------")
    operation_choice=show_menu()
    if operation_choice==1:
        x,y=userPrompt()
        result=add(x,y)
        print(f"Result: {result}")
    elif operation_choice==2:
        x,y=userPrompt()
        result=subtract(x,y)
        print(f"Result: {result}")
    elif operation_choice==3:
        x,y=userPrompt()
        result=multiply(x,y)
        print(f"Result: {result}")
    elif operation_choice==4:
        x,y=userPrompt()
        result=divide(x,y)
        print(f"Result: {result}")
    elif operation_choice==5:
        pass

quit=False
while not quit:
    main()
    wants_to_quit = input("Wants to Quit? 'y' to confirm, any other character otherwise.")
    if wants_to_quit.lower()=='y':
        quit=True    
print("\n---------end--------")
   



