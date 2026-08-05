##





passenger = int(input('enter number of passenger:'))
ticket = float(input('enter ticket price:'))

total = 0

for i in range(passenger):
    age = int(input('enter ahe of passenger:'))
    
    if age<12:
        price = ticket - (ticket  * 0.30)
    elif(age > 59):
        price = ticket - (ticket * 0.50)
    else:
        price = ticket
        
    total = price
    
print('total price: ',total)            
            