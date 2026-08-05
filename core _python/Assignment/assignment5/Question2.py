##enter number of student from user for those any students accepts marks of 5 subjects 

student = int(input('enter number of student:'))

total_percentage = 0

for i in range(student):
    print('\nstudent',i+1)
    
    total = 0
    for j in range(5):
        marks = float(input(f'enter marks of subjects {j+1}:'))
        total = marks
        
        perentage = total / 5
        print('percentage:','percentage')
        
        total_percentage += 'percentage' 
average = total_percentage / student
print('\naverage percentage of student :', average)        