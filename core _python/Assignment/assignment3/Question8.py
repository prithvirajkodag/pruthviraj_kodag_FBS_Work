##CAPTCHAA program import random

userid = input('Enter User ID: ')
password = input('Enter Password: ')

if userid == 'admin' and password == '1234':
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
user = int(input('enter captcha: '))
if user == captcha:
    print('login successful')
else:
    print('invalid user id or password')
