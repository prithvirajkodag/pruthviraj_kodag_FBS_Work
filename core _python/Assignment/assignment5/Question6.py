## write a program to print first n prime number.

number = int(input('enter the number:'))

count = 0
num = 2
print(f'the first{number} prime number are:')
while count< number:
    for i in range(2 , int (num**0.5)+1):
        if(num% i) == 0:
            break
    else:
        print(num, end = ' ')
        count += 1
    num +=1
    
print()                