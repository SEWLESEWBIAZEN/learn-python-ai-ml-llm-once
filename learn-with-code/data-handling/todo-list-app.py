import json, os

# file for storing tasks
TASK_FILE = "my_tasks.json"

if not os.path.exists(TASK_FILE):
    with open(TASK_FILE,'w') as json_file:
        json.dump([], json_file)

# step 1. load tasks from json
# Load existing tasks from file, or return an empty list if file doesn't exist
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as json_file:
        try:
            return json.load(json_file)
        except json.JSONDecodeError:
            return []
    
# Step 2. Save tasks to json
def save_tasks(tasks):
    with open(TASK_FILE,'w') as json_file:
        json.dump(tasks,json_file,indent = 2)

# Step 3. Add new task
# Add a new task
def add_task():
    task_name = input("Enter task name: ")
    tasks = load_tasks()
    tasks.append({"task": task_name, "status": "Incomplete"})
    save_tasks(tasks)
    print(f"Task '{task_name}' has been added successfully!")


# Step 4. View all tasks
def view_tasks():
    tasks=load_tasks()
    if tasks:
        print("\n----To-Do List---------")
        for idx,task in enumerate(tasks,start=1):
            print(f"{idx}. {task['task']} - {task['status']}")
    else:
        print("No task found!")

# Step 5 update tasks status

def update_task_status():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index=int(input("Enter the task number"))
        if 0<=task_index<len(tasks):
            new_status = input("Enter the new status (Complete/InComplete): ").strip()
            tasks[task_index]['status'] = new_status
            save_tasks(tasks)
        
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


# Step 6: Delete Task
def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        task_index = int(input("Enter task index you want to delete: "))
        if 0<=task_index<len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"{deleted_task['task']} deleted Successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Step 7. Display Menu
def display_menu():
    print("\n------Mini To-Do Menu----------")
    print("1. Add new Task.")
    print("2. View all tasks.")
    print("3. Update task status")
    print("4. Delete task")
    print("5. Exit")


# Main loop
def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:              
               add_task()
            elif choice == 2:              
               view_tasks()
            elif choice == 3:
                update_task_status()
            elif choice == 4:
                delete_task()
            elif choice == 5:                
                print("All done! Thank you.")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"Error: {e}")

# Run the program
if __name__ == "__main__":
    main()
