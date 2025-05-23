
# defining the file
JOURNAL = 'Readme.md'

# Step 1. add entry, writing to the file
def add_entry():
    entry = input("Enter your entry:")
    try:
        with open(JOURNAL,'a') as file:
            file.write(entry)
            print("Entry is added successfully.")
    except:
        print("Error occurred while writing the journal.")

# Step 2. read all contents, reading all
def view_entries():
    try:
        with open(JOURNAL, 'r') as file:
            content = file.read()
            print("\n------------Journal Entries----------------")
            print(content)
    except:
        print("Error occured while reading the journal.")

# Step 3. Search an item from the content
def search_entry():
    
    search_term = input("Enter search term")
    try:
        with open(JOURNAL,'r') as file:
            contents = file.readlines()
            for content in contents:
                if content.__contains__(search_term):                  
                    print("\n------Found Content----------")
                    print(content)
                else:                    
                    print("No Search content found!")
    except:
        print("Error occured while searching a content!")


# step 4. mehu
def show_menu():
    print("\n------Select from 1-4-----------")
    print("1. To Register your daily Journal")
    print("2. To view all journals")
    print("3. Search content")
    print("4. exit")


# Step 5. main method
def main():
    while True:
        show_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if(choice == 1):
                add_entry()
            elif(choice== 2):
                view_entries()
            elif(choice == 3):
                search_entry()
            elif(choice == 4):
                print("You all done! Thank you.")
                break
        except:
            print("Error occured while accepting user choice: ")
            main()


main()