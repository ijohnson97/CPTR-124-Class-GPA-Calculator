## Name: Ian Johnson
## Date Last Modified: 9.13.16
## Program: Class GPA Calculator
## Purpose: User enters in students' letter grades for a class, which the code then converts to a Class Average GPA
## Honesty Statement: I neither gave nor recieved unauthorized help on this code.

grades = []

letter = input('Enter letter grades ("Z" terminates the list):\n').upper()

while(letter != 'Z'):
    if letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D' or letter == 'F':
        grades.append(letter)
    letter = input().upper()

failed = grades.count('F')
passed = len(grades) - failed

totalGPA = grades.count('A')*4.0 + grades.count('B')*3.0 + grades.count('C')*2.0 + grades.count('D')

print('Students Passed:',passed,'({:.2f}%)'.format((passed/len(grades))*100))
print('Students Failed:',failed,'({:.2f}%)'.format((failed/len(grades))*100))
print('Class GPA: {:.2f}'.format(totalGPA/len(grades)))