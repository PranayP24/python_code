#Compare two numbers using relational operators
num1=int(input('enter the dividend value:'))
num2=int(input('enter the divisor value :'))
result=""
for i in range(num1-num2):
    result+=">"
    break
print(num1,result,num2)
i =0
while i < num1-num2:
    result+=">"
    break
print(num1,result,num2)
