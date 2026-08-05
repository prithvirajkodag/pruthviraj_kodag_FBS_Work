## N + n^2 + n^3+n^4..+n^n(here ^ means exponent)

n = int(input('enter n:'))

sum = 0 
for i in range(1 , n+1):
    sum += n ** i
    
print('sum : ', sum)    