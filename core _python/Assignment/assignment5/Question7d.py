## S = a + a2 / 2 + a3 / 3 + ...+ a10 / 10

n = int(input('enter value of a for series d:'))

total_sum = 0
for i in range(1 , 11):
    total_sum = total_sum + (n**i)/i
print(f'sum of series d:{total_sum}')
print()    