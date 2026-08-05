##write a program to solve the follpwing series :
# a.1! + 2! +3! 4! + ...n!

n = int(input('enter n series for a:'))
total_sum = 0
fact = 1
for i in range(1 , n + 1):
    fact = fact * i 
    total_sum +=fact
print(f'sum of series a:{total_sum}')    