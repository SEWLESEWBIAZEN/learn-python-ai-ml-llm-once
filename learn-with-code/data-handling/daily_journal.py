
# defining the file
JOURNAL = '../../README.md'

# defining entry type selection
def show_entry_type():
    print("\n------Select from 1-4-----------")
    print("1. Title.")
    print("2. Subtitle.")
    print("3. Description.")
    print("4. exit")    

# format entry based on their type.
def format_entry():
    while True:
        show_entry_type()
        try:
            entry_type = int(input("\nEnter your type: "))
            if(entry_type == 1):
                entry_text = input("Type here: ")
                formatted_text = f"\n\n {entry_text}\n"
                add_entry(formatted_text)
            elif(entry_type== 2):
                entry_text = input("Type here: ")
                formatted_text = f"\n {entry_text}\n"
                add_entry(formatted_text)
            elif(entry_type == 3):
                entry_text = input("Type here: ")
                formatted_text = f"{entry_text}\n"
                add_entry(formatted_text)
            elif(entry_type == 4):
                print("You all done! Thank you.")
                break
        except:
            print("Error occured while accepting user choice: ")          
       

# Step 1. add entry, writing to the file            
def add_entry(entry):
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
    found_content = ""
    search_term = input("Enter search term:").lower()
    try:
        with open(JOURNAL,'r') as file:
            contents = file.readlines()
           
            for content in contents:
                if search_term in content.lower():
                    print(content)
                    found_content+=f"\n{content}"                              
                else:
                    pass                  
    except:
        print("Error occured while searching a content!")
    if(found_content!=""):
        print("\n------Found Content----------")
        print(found_content)   
    else:
        print("No Search content found!")

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
                format_entry()
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

# calling main method
main()