# ============================================================
# LESSON: PYTHON LISTS – ADDING, MODIFYING, SORTING & LOOPING
# ============================================================

# -------------------------------
# PART 1: CREATING AND MODIFYING LISTS
# -------------------------------

# Initial list of fruits
ice_list = ['Apple', 'Grapes', 'Lemon', 'Orange']
print("Initial List:", ice_list)  # Displays the starting list

# Adding an element to the END of the list using append()
ice_list.append('ONE')
print("After append('ONE'):", ice_list)

# Inserting an element at a specific index using insert()
# Syntax: list.insert(index, value)
ice_list.insert(2, 'ICE')  # 'ICE' will be placed at index 2
print("After insert(2, 'ICE'):", ice_list)

# -------------------------------
# PART 2: SORTING LISTS
# -------------------------------

# Sorting in ascending order (A → Z)
ice_list.sort()
print("Sorted Ascending:", ice_list)

# Sorting in descending order (Z → A)
ice_list.sort(reverse=True)
print("Sorted Descending:", ice_list)

# Using sorted() to create a NEW sorted list (does not change original)
new_sorted_list = sorted(ice_list, reverse=True)
print("New Sorted List (Descending):", new_sorted_list)

# Copying a list (note: this is just a reference copy)
new_sorted_list = ice_list
print("Copied List:", new_sorted_list)


# ============================================================
# PART 3: LOOPING THROUGH LISTS (MULTIPLE WAYS)
# ============================================================

# Creating separate lists
drinks = ['Coke', 'Sprite', 'Tup', 'Pepsi']
snacks = ['Pizza', 'Burger', 'Hotdog']
dessert = ['Cake', 'IceCream']

# Combining multiple lists into a tuple
food = (drinks, snacks, dessert)
print("\nFood Tuple:", food)  # Shows all three lists together

# -------- Version 1: Simple For Loop --------
print("\nVersion 1 - Simple Loop:")
for item in drinks:
    print(item, end=' ')
print()  # Newline

# -------- Version 2: Looping by Index in Reverse Order --------
print("\nVersion 2 - Reverse Order by Index:")
for i in range(len(drinks) - 1, -1, -1):
    print(drinks[i], end=' ')
print()  # Newline

# -------- Version 3: Using enumerate() to get index and value --------
print("\nVersion 3 - Using enumerate():")
for index, value in enumerate(drinks):
    print(f'{index} = {value}', end=' ')
print()  # Newline

# ============================================================
# LESSON SUMMARY:
# 1. append() → adds to end of list
# 2. insert(index, value) → adds at a specific position
# 3. sort() → changes list order permanently
# 4. sorted() → returns a new sorted list (original unchanged)
# 5. enumerate() → gives index + value during iteration
# 6. range() with negative step → loops backward
# ============================================================


# Multiplication Table - 3 Versions
# Lesson Notes:
# This script demonstrates three different ways to create and display a multiplication table.
# It covers:
#   - Using loops without storing values in a list
#   - Using nested loops to store results in lists
#   - Using list comprehension for concise code





# ---------------------------
# Version 1: Without a List
# ---------------------------
# This version prints the multiplication table directly without saving the results.
# It uses nested for loops and the print() function to format the output.
for x in range(1, 6):  # Outer loop controls the 'x' value (1 to 5)
    for y in range(1, 11):  # Inner loop controls the 'y' value (1 to 10)
        # f-string formats the output; end='' prevents new line after each print
        print(f'{x * y: <3}', end='')  
    print()  # Move to the next line after finishing one row

# ---------------------------
# Version 2: Using Lists
# ---------------------------
# This version stores the multiplication results in a nested list (list of lists).
multiply_table = []  # Empty list to hold the table

for x in range(1, 6):
    tmp = []  # Temporary list for each row
    for y in range(1, 11):
        tmp.append(x * y)  # Append the multiplication result to the row
    multiply_table.append(tmp)  # Append the row to the main table

# Print the entire multiplication table list
print(multiply_table)

# ---------------------------
# Version 3: List Comprehension
# ---------------------------
# This version uses list comprehension for a compact way to create the table.
multiply_table = [[x * y for y in range(1, 11)] for x in range(1, 6)]

# Print the multiplication table
print(multiply_table)
