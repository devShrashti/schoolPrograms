import pickle

# Function to add a record to shoes.dat
def add_record():
    try:
        with open("shoes.dat", "ab") as file:
            pcode = input("Enter Product Code: ")
            pname = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            rating = int(input("Enter Product Rating (1-10): "))
            bid = input("Enter Brand ID: ")
            record = {"PCode": pcode, "PName": pname, "UPrice": price, "Rating": rating, "BID": bid}
            pickle.dump(record, file)
            print("Record added successfully!")
    except Exception as e:
        print("Error:", e)

# Function to display all records from shoes.dat
def display_records():
    try:
        with open("shoes.dat", "rb") as file:
            print("\nDisplaying all records:\n")
            while True:
                try:
                    record = pickle.load(file)
                    print(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

# Function to search for a record by Product Code
def search_record():
    try:
        pcode_search = input("Enter Product Code to search: ")
        found = False
        with open("shoes.dat", "rb") as file:
            while True:
                try:
                    record = pickle.load(file)
                    if record["PCode"] == pcode_search:
                        print("\nRecord Found:", record)
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            print("No record found with Product Code:", pcode_search)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)

# Menu-driven program
while True:
    print("\nMenu:")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Search Record by Product Code")
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
