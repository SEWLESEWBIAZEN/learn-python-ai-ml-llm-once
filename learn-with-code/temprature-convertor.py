def find_units(base,to,x):
    result=0
    units=[
        {
            "name":"celsius",
            "to":"fahrenheit",
            "calculation":((x*(9/5))+32)
        },
        {
            "name":"celsius",
            "to":"kelvin",
            "calculation":(x+273.15)
        },
        {
            "name":"fahrenheit",
            "to":"kelvin",
            "calculation":((x-32)*(5/9)+273.15)
        },
        {
            "name":"kelvin",
            "to":"celsius",
            "calculation":(x-273.15)
        },
        {
            "name":"kelvin",
            "to":"fahrenheit",
            "calculation":((x-273.15)*(9/5)+32)
        },
    ]

    for item in units:
        if(item['name'].lower()==base.lower() and item['to'].lower()==to.lower()):
            result=item['calculation']
    return result

def choice_input(type):
   output= int(input(f"{type}:"))
   if output==1:
       return "celsius"
   elif output==2:
       return "fahrenheit"
   elif output==3:
       return "kelvin"
   else:
      exit()

def user_helper():
   print("-------Legend--------")
   print("1. celsius.")
   print("2. fahrenheit.")
   print("3. kelvin")
   base=choice_input("From")
   to = base
   while base==to:
    to=choice_input("To")
    if base==to:
       print("both from and to can not be the same unit, try again")


   return base,to

print("-------------start----------------\n")
base,to=user_helper()
base_value = float(input(f"Enter the value in {base} to convert the temprature {to}: "))
f_result=find_units(base,to,base_value)
print(f"Final result({to}): {f_result:.2f}")
print("\n---------------end---------------------")






