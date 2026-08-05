##write a program to print prime number between 1 to 100

print ('prise number fom 1 to 100:')

for i in range (1,100):
    if i>1:
        for j in range(2,int(i **0.5)+1):
            if(i % j)==0:
                break
        else:
            print(i,end=' ')    