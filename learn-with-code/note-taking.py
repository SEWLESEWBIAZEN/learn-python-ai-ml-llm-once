
def show_choice():
    print("----Choice----")
    print("1. Add Note.")
    print("2. View Note.")
    print("3. Delete Note.")
    print("q. Exit.")

def addNote(file):
    with open(file,"a") as file:
        note=input("Enter Your Note: ")
        file.write(f"\n{note}")
        print("Note Added Successfully!")
    
def viewNote(file):
    with open(file,"r") as file:
        content = file.read()
        if content: 
            print("\n----My Notes----")
            print(content)
        else:
            print("No Note Availabel!")

def deleteNote(file):
    confirm = input("Are you sure to delete all note? Enter 'y' yes/no: ")
    if confirm.lower()=="y":        
        with open(file,"w") as file:
            pass
        print("All note have been deleted!")
    else:
        print("Delete Note Cancelled")

quit = False
while not quit: 
    show_choice()  
    user_choice = input("\nEnter 1 through 3, or q to exit: ")
    if user_choice == '1':
        addNote("myNotes.txt")
    elif user_choice == '2':
        viewNote("myNotes.txt")
    elif user_choice =='3':
        deleteNote("myNotes.txt")
    else:
        print("Invalid user choice!")
    
    user_choice_to_continue = input("\nWants to quit? Enter 'y' to continue: ")
    if user_choice_to_continue.lower() == 'y':
        quit = True
    else:
        continue

viewNote("myNotes.txt")

