##write a program to input two angles from user and find thrd angle of the 
##triangle

angle1 = int(input ("enter first angle of triangle: "))
angle2 = int(input("enter second angle of triangle:"))
angle3 = 180 - (angle1 + angle2)
print("third angle of triangle is:", angle3)