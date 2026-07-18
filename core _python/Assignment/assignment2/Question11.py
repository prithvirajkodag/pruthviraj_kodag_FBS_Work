##witw a program to accept an integer amount from user and tell minimum numbr of notes needed for representing that amount

amount = int(input('enter amount:'))
n500 = amount // 500
amount = amount % 500
n200 = amount // 200
amount = amount % 200
n100 = amount // 100
amount = amount % 100
n50 = amount // 50
amount = amount % 50
n20 = amount // 20
amount = amount % 20
n10 = amount // 10
amount = amount % 10
n5 = amount // 5 
amount = amount % 5 
print(f' 500 Notes = {n500}:')
print(f' 200 Notes = {n200}:')
print(f' 100 Notes = {n100}:')
print(f' 50 Notes = {n50}:')
print(f' 20 Notes = {n20}:')
print(f' 10 Notes = {n10}:')
print(f' 5 Notes = {5}:')