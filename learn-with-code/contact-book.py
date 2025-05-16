import re

contacts = {}
phone_pattern = r"^(\+\d{12}|0(9|7)\d{8})$" 
name_pattern = r"^[A-Za-z]{5,50}$"
email_pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"


def add_contact():
    unVerified = True
    while(unVerified):        
        unVerified_name = input("Enter contact name:")
        if re.match(name_pattern,unVerified_name):
            name=unVerified_name
            unVerified=False
        else:
            print("Invalid name input, try again.")

    unVerified= True
    while(unVerified):
        phone_unverified = input("Enter contact number:")
        if re.match(phone_pattern, phone_unverified):
            phone = phone_unverified
            unVerified=False
        else:
            print("Invalid input, Enter Again")

    unVerified=True
    while(unVerified):                       
        unVerified_email = input("Enter contact email: ")
        if re.match(email_pattern,unVerified_email):
            email = unVerified_email
            unVerified=False
        else:
           print("Invalid input, Enter Again") 
    
    
    contacts[name]= { "phone":phone,"email":email}  

toContinue = True
while(toContinue):    
    add_contact()
    input_text=input("Enter q to quit: ")
    if(input_text == 'q'):
        toContinue=False 

for name,details in contacts.items():
    print("")
    print (f"Name: {name}")   
    print (f"Phone:{details['phone']}")
    print (f"Email: {details['email']}")


