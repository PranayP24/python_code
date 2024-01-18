#Use the modulo operator to check for even numbers
num=int(input('enter the value:'))
for i in range(num):
    if num%2==0:
        print('Number is even :True')
        break
    else:
        print('number is not even : False')
        break
while num%2==0:
    print('number is even')
    num+=1
