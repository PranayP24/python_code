#Find the sum of all numbers in a list
numbers=[1,2,3,4,5]
sum_of_numbers=0
for num in numbers:
    sum_of_numbers+=num
print(sum_of_numbers)
num=0
while num < len(numbers):
    sum_of_numbers+=numbers[num]
    num+=1
print(sum_of_numbers)
