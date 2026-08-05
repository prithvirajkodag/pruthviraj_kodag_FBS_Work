## find the sum of geomatric series from 1 to n whre the common ratio is 2

n = int(input('enter number n:'))

sum = 0 

for i in range(n):
    sum += 2 ** i 
    
print('sum =', sum)    
    