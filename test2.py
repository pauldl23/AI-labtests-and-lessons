student = input('Enter student name: ')
gender = input('student gender (m/f): ').lower()

if gender != 'm' and gender != 'f':
    print ('Invalid gender. You must enter m or f')
    exit()

grades = input('Input 3 grades (comma-separated): ')
c1 = grades.find(',')
c2 = grades.find(',', c1+1)

if c1 == -1 or c2 == -1 or grades.find(',', c2+1) != -1:
    print('Invalid grade. You must enter exactly 3 numbers between 60 and 100'); 
    exit()

g1 = float(grades[:c1])
g2 = float(grades[c1+1:c2])
g3 = float(grades[c2+1:])

except ValueError:
    print('Invalid grade. You must enter exactly 3 numbers between 60 and 100'); 
    exit()

if not all(60 <= g <= 100 for g in [g1, g2, g3]):
    print('Invalid grade. You must enter exactly 3 numbers between 60 and 100'); 
    exit()

avg = round((g1 + g2 + g3) / 3, 2)
print('Student name:', student)
print('Gender:', gender)
print('Average:', avg)
print('Remark:', ['Satisfactory','Good','Very Good','Excellent'][(avg >= 90)+(avg >= 80)+(avg >= 70)])