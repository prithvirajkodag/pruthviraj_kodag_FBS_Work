##check wether the a triangle is valid using angles 

a = int(input("enter first angle:"))
b = int(input("enter second angle:"))
c = int(input("enter third angle:"))
if a + b + c ==180:
    print("valid triangle")
else:
    print("invalid triangle")  