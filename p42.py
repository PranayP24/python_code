#Calculate the sum of two numbers

num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
sum=0
for i in range(1):
     sum=num1+num2
print("The sum of num1 and num2 is: ",sum)

num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
sum=0
for i in range(num1):
     sum=num1+num2
     break
print("The sum of num1 and num2 is: ",sum)
