#Find the maximum number in a list
numbers=[3, 1, 4, 1, 5, 9, 2]
max_number=numbers[0]
for num in numbers:
    if num > max_number:
        max_number=num
print(max_number)
num =0
while num < len(numbers):
    if num > max_number:
        max_number=num
    num+=1
print(max_number)
