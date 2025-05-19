import random, string
# strong password generation
def generate_strong_password(length):
    print("It includes Lower case, UPPER CASE, digits and punctuations.")
    string_pool=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)              

    ]  
    password_string=finish_password(password,string_pool,length-4)
    return password_string

# medium strong password generation
def generate_medium_password(length):
    print("It includes Lower case, UPPER CASE and digits.")
    string_pool=string.ascii_lowercase + string.ascii_uppercase + string.digits 
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits)                 
    ] 

    password_string=finish_password(password,string_pool,length-3)   
    return password_string

#  less strong password generation
def generate_weak_password(length):
    print("It includes only letters and digits.")
    string_pool=string.ascii_letters + string.digits
    password = [
        random.choice(string.ascii_letters),        
        random.choice(string.digits)                   
    ]  
    password_string=finish_password(password,string_pool,length-2)  
    return password_string

# finishes the password by concatinating the array of characters to actual password string
def finish_password(password,string_pool,remaining_length):
    password+=random.choices(string_pool,k=remaining_length)
    random.shuffle(password)
    return ''.join(password)

# main entry method
def generate_password(strength,length):
    if length < 4:
        print("Invalid Password Length")
        exit()
    if(strength == '1'):
        password=generate_strong_password(length)
    elif(strength == '2'):
        password=generate_medium_password(length)
    elif (strength == '3'):
        password=generate_weak_password(length)
    else: 
        password=generate_strong_password(length)
    print(f"\nPassword: {password}\n")
    print("----------------------------------------------------")

print("----------------START-----------------------")

length = input("Enter the length of password you wants to generate:\n")
# no length input provided from user, take the default password length which is 8
if length!='':
    length = int(length)
else:
    length=8

print("------------Please select the strength of your password.------------")
print("1. Strong")
print("2. Medium")
print("3. Weak")
strength = input("Enter the strength of the password you are going to generate:\n")


generate_password(strength,length)
