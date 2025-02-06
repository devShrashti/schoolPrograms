import csv

# Function to add a record to telephone.csv
def add_record():
    try:
        with open("telephone.csv", "a", newline="") as file:
            writer = csv.writer(file)
            empid = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            dob = input("Enter Date of Birth (DD-MMM-YYYY): ")
            deptid = input("Enter Department ID: ")
            design = input("Enter Designation: ")
            salary = input("Enter Salary: ")
            writer.writerow([empid, name, dob, deptid, design, salary])
            print("Record added successfully!")
    except Exception as e:
        print("Error:", e)

# Function to display all records from telephone.csv
def display_records():
    try:
        with open("telephone.csv", "r") as file:
            reader = csv.reader(file)
            print("\nDisplaying all records:\n")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

# Function to search for a record by Employee ID
def search_record():
    try:
        empid_search = input("Enter Employee ID to search: ")
        found = False
        with open("telephone.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == empid_search:
                    print("\nRecord Found:", row)
                    found = True
                    break
        if not found:
            print("No record found with Employee ID:", empid_search)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

# Menu-driven program
while True:
    print("\nMenu:")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Search Record by Employee ID")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_record()
    elif choice == 2:
        display_records()
    elif choice == 3:
        search_record()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
