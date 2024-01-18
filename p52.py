#Calculate the factorial of a number
fact_number=int(input('enter the factorial of a number:'))
factorial=1
for num in range(1,fact_number+1):
    factorial=factorial*num
print(factorial)
num =1
while num <= fact_number:
    factorial=factorial*num
    num+=1
print(factorial)
