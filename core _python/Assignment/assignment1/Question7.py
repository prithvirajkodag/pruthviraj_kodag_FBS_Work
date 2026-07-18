 ##program to find the roots of a quadratic equation
import cmath
 
a = float(input("enter coefficient a: "))
 
b = float(input("enter coefficent b: "))
           
c = float(input("enter coefficent c: "))
                  
# calculate the discriminant
d = (b**2) - (4*a*c)

# find the two roots
root1 = (-b - cmath.sqrt(d)) /(2*a)
root2 = (-b + cmath.sqrt(d)) /(2*a) 

print("the roots are{0} and {1}".format(root1, root2))               