##write a programto enter P, T, R and calculate compound interest

P = float(input("enter principal amount: "))

T = float(input("enter the time in years:"))

R = float(input("enter the rate of interest: ")) 

Z = P * (1 + R/100)**  T - P

print("compound interest is:", Z) 