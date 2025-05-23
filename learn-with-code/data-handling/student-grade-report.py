import csv
import os
import re

# Helper: Validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Create new CSV file
def create_csv(file_name=None):
    print("\n-------WELCOME TO CREATE NEW CSV FILE-------")
    if not file_name:
        file_name = input("Filename: ")
    file_headers = ["Name", "Sex", "Email", "Mathes", "English", "Science", "Programming", "Average", "Status"]
    with open(f"{file_name}.csv", 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(file_headers)
    print(f"File '{file_name}.csv' created successfully.")

# Get score input with validation
def score_input(course):
    try:
        score = float(input(f"Enter {course} Score: "))
        return score
    except ValueError:
        print("Invalid input. Try again.")
        return score_input(course)

# Add new record to existing file
def add_new_record():
    print("\n-------WELCOME TO ADD NEW RECORD-------")
    filename = input("Filename: ")
    
    if os.path.exists(f"{filename}.csv"):
        with open(f"{filename}.csv", 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
            expected_headers = ["Name", "Sex", "Email", "Mathes", "English", "Science", "Programming", "Average", "Status"]
            if headers != expected_headers:
                print("File headers do not match expected structure.")
                return

        while True:
            print("\n--------Enter Row Values-----------")          
            name = input("Enter the name of the student: ")
            sex = input("Gender: ")

            while True:
                email = input("Email: ")
                if is_valid_email(email):
                    break
                print("Invalid email format. Try again.")

            mathes_score = score_input("Mathematics")
            english_score = score_input("English")
            science_score = score_input("Science")
            programming_score = score_input("Programming")
            average = round((mathes_score + english_score + science_score + programming_score) / 4, 2)
            status = "Pass" if average >= 60 else "Fail"

            with open(f"{filename}.csv", 'a', newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([name, sex, email, mathes_score, english_score, science_score, programming_score, average, status])            

            again = input("Enter 1 to exit, 2 to add another: ")
            if again == '1':
                break
    else:
        print("File does not exist!")
        want_to_create = input("1. Create file\n2. Exit\nEnter choice: ")
        if want_to_create == '1':
            create_csv(filename)
        else:
            print("Exiting...")

# Optional: Search student record
def search_entry():
    filename = input("Filename: ")
    if os.path.exists(f"{filename}.csv"):
        keyword = input("Enter name or email to search: ").lower()
        found = False
        with open(f"{filename}.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if any(keyword in str(cell).lower() for cell in row):
                    print(row)
                    found = True
        if not found:
            print("No matching records found.")
    else:
        print("File not found.")

# User menu
def show_menu():
    print("\n------Select from 1-4-----------")
    print("1. Create new CSV file.")
    print("2. Add records")
    print("3. Search records")
    print("4. Exit")

# Main loop
def main():
    while True:
        show_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:              
               create_csv()
            elif choice == 2:              
               add_new_record()
            elif choice == 3:
                search_entry()
            elif choice == 4:
                print("All done! Thank you.")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"Error: {e}")

# Run the program
if __name__ == "__main__":
    main()
