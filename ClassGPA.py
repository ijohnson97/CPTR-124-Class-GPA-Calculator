## Name: Ian Johnson
## Date Last Modified: 9.9.16
## Program: Class GPA Calculator
## Purpose: User enters in students' letter grades for a class, which the code then converts to a Class Average GPA
## Honesty Statement: I neither gave nor recieved unauthorized help on this code.

grades = []     ## list of all letter grades
grade = 0

letter = input('Enter grades. (Z terminates the list):\n').upper()

while(letter != 'Z'):
    grades.append(letter)
    letter = input().upper()

# Need to weed out invalid enteries

while(grade < len(grades)):
    if grades[grade] != 'A' and grades[grade] != 'B' and grades[grade] != 'C' and grades[grade] != 'D' and grades[grade] != 'F':
        del grades[grade]
        grade = 0 
    else:
        grade += 1
    
failed = grades.count('F')
passed = len(grades) - failed
percPassed = passed/len(grades)
percFailed = failed/len(grades)

totalGPA = grades.count('A')*4.0 + grades.count('B')*3.0 + grades.count('C')*2.0 + grades.count('D')
classGPA = totalGPA/len(grades)

print('Students passed:',passed,'({:.2f}%)'.format(percPassed*100))
print('Sutdents failed:',failed,'({:.2f}%)'.format(percFailed*100))
print('Class GPA: {:.2f}'.format(totalGPA/len(grades)))