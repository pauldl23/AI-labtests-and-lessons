tup1=()
print(tup1)

#method2
tup2=(1,2,3,'apple','Banana')
print(tup2)

#method3
single_tuple=(1)
print(type(single_tuple))

#method4
tup3 = 11,12,23
print(type(tup3),tup3)

#method5
tup4 = tuple([1,2,3])
print(type(tup4),tup4)

tup5 = tuple('abc')
print(type(tup5),tup5)
single_tuple = tuple("1")

tup6=tuple(range(5,11))
print(type(tup6), tup6)

tup8 = (1,(2,3),(4,5))
print(type(tup8),tup8)
print(tup8[2][1])
print('+'*20)

    
for i, row in enumerate(tup8):
    print(f'ROW: {i} VALUE:{row}')
    if isinstance(row, (tuple, list)):
        for value in row:
            print(f'    value: {value}')
    else:
        print(f'    value: {row}')
        
        
        
 # Remove value from tuple
tup = (4, 5, 6, 7)
print("Before:", tup)
tup = tup[:2] + tup[3:]   # removes the 3rd element (6)
print("After:", tup)

# Insert value into tuple
tup = (10, 20, 30, 40)
print("Before:", tup)
tup = tup[:2] + (25,) + tup[2:]  # insert 25 at index 2
print("After:", tup)

# Remove value from another tuple
tup = (10, 200, 300, 400)
print("Original tuple:", tup)
tup = tup[:1] + tup[2:]   # removes 200
print("After removing:", tup)





#anothercode

# Employee data stored as tuples
employees = (
    ("Alice Go", "Software Engineer", 8000),
    ("Johnny Pol", "Contractor", 590809),
    ("Angel", "Wifey", 50)
)

# Function to display employees
def display_employees(employee_list):
    print("Employee List:")
    for employee in employee_list:
        print(f"Name: {employee[0]}, Position: {employee[1]}, Salary: {employee[2]}")

# Main program
if __name__ == "__main__":
    display_employees(employees)
