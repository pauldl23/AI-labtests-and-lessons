# ------------------------------------------
# 🧠 PYTHON CRUD PROGRAM USING DICTIONARIES
# Create, Read, Update, Delete (and more!)
# ------------------------------------------

# Initial data (dictionary of dictionaries)
people = {
    1: {'name': 'a', 'age': 21, 'gender': 'male'},
    2: {'name': 'b', 'age': 25, 'gender': 'female'},
    3: {'name': 'c', 'age': 30, 'gender': 'male'}
}

# Infinite loop for the main menu
while True:
    print("\n===== MENU =====")
    print("[1] Add\t\t[2] Edit")
    print("[3] Delete\t[4] Reset")
    print("[5] Display\t[6] Search")
    print("[0] Exit")

    choice = input("Enter choice: ")

    # --------------------------
    # 1️⃣ ADD RECORD
    # --------------------------
    if choice == '1':
        key = max(people.keys()) + 1 if people else 1  # auto-generate next ID
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")

        # store data in dictionary
        people[key] = {'name': name, 'age': age, 'gender': gender}
        print("✅ Record added successfully!")

    # --------------------------
    # 2️⃣ EDIT RECORD
    # --------------------------
    elif choice == '2':
        key = int(input("Enter ID to edit: "))
        if key in people:
            # Allow the user to keep old values if they press Enter
            name_input = input(f"Enter new name ({people[key]['name']}): ") or people[key]['name']
            age_input = input(f"Enter new age ({people[key]['age']}): ") or people[key]['age']
            gender_input = input(f"Enter new gender ({people[key]['gender']}): ") or people[key]['gender']

            # Update dictionary
            people[key]['name'] = name_input
            people[key]['age'] = age_input
            people[key]['gender'] = gender_input

            print("✅ Record updated successfully!")
        else:
            print("❌ ID number not found!")

    # --------------------------
    # 3️⃣ DELETE RECORD
    # --------------------------
    elif choice == '3':
        key = int(input("Enter ID to delete: "))
        if key in people:
            del people[key]
            print("🗑️ Record deleted successfully!")
        else:
            print("❌ ID not found!")

    # --------------------------
    # 4️⃣ RESET ALL DATA
    # --------------------------
    elif choice == '4':
        confirm = input("Are you sure you want to reset all data? (y/n): ").lower()
        if confirm == 'y':
            people.clear()  # remove all records
            print("⚠️ All records cleared!")
        else:
            print("Action canceled.")

    # --------------------------
    # 5️⃣ DISPLAY ALL RECORDS
    # --------------------------
    elif choice == '5':
        if not people:
            print("⚠️ No records to display.")
        else:
            print("\n📋 CURRENT RECORDS:")
            print("-" * 40)
            for id, info in people.items():
                print(f"ID: {id} | Name: {info['name']} | Age: {info['age']} | Gender: {info['gender']}")
            print("-" * 40)

    # --------------------------
    # 6️⃣ SEARCH RECORD BY NAME
    # --------------------------
    elif choice == '6':
        search = input("Enter name to search: ")
        found = False
        for id, info in people.items():
            if info['name'].lower() == search.lower():  # case-insensitive match
                print(f"🔍 Found → ID: {id}, Age: {info['age']}, Gender: {info['gender']}")
                found = True
        if not found:
            print("❌ No record found.")

    # --------------------------
    # 0️⃣ EXIT PROGRAM
    # --------------------------
    elif choice == '0':
        print("👋 Exiting program... Goodbye!")
        break  # exits the while loop

    # --------------------------
    # INVALID INPUT
    # --------------------------
    else:
        print("⚠️ Invalid choice! Please enter a number from 0 to 6.")
