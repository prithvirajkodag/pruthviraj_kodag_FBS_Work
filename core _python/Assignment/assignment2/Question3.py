##convert distance given fet and inches into meter and centimeter

Feet = int(input('enter feet:'))
inches = int(input('enter inches:'))
total_inches = (Feet * 12) + inches 
meter = total_inches * 0.0254
centimeter = meter * 100 
print(f'meter = {meter} and centimeter = {centimeter}')