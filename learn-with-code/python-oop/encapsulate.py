
class Person:
    def __init__(self, email, password,name):
        self.__name=name
        self.__email=email
        self.__password=password

    def set_email(self,new_email):
        self.__email=new_email

    def set_name(self,new_name):
        self.__name=new_name
    
    def set_password(self,new_password):
        self.__password=new_password


    def get_email(self):
        return self.__email
    
    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password
    

   
def main():
    person = Person("sewlesewbiazen65@gmail.com","Sewlesew@12","Sewlesew Biazen")
    print(person.__name)
    print(person.get_name())
    print(person.get_password())
    print(person.get_email())
    person.set_name("Sewlesew2")
    print(person.get_name())

# if __name__== main:
main()
