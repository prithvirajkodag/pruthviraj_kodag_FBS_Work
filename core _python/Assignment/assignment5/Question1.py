##write a program to promot user to enter userid and password if id and password 
#is incorrect give him chance to re-enter the credential let him try 3 times after that program o terminate 

userid = 'raj'
password = '@1234'

for i in range(4):
    userid1 = input('enter userid:')
    password = input('enter password:')
    
    if userid == userid and password == password:
         print('login succesfully:')
         break
    else:
        print('wrong userid and password')
        remaining = 3-i
        print('incorrect crediential remaining attempts',remaining)
else:
    print('program terminate because of too many attempts')         