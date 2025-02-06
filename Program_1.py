import pickle

# Function to create and add employee records
def Create():
    try:
        with open("employee.dat", "ab") as file:
            empid = int(input("Enter Employee ID: "))
            ename = input("Enter Employee Name: ")
            designation = input("Enter Designation: ")
            record = {"Empid": empid, "EName": ename, "Designation": designation}
            pickle.dump(record, file)
            print("Record added successfully!")
    except Exception as e:
        print("Error:", e)

# Function to display records where Empid > 101
def Display():
    try:
        with open("employee.dat", "rb") as file:
            print("\nEmployees with Empid > 101:\n")
            while True:
                try:
                    record = pickle.load(file)
                    if record["Empid"] > 101:
                        print(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

# Menu-driven program
while True:
    print("\nMenu:")
    print("1. Add Employee Record")
    print("2. Display Employees with Empid > 101")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        Create()
    elif choice == 2:
        Display()
    elif choice == 3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
