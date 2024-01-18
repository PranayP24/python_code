#Find the second largest number in a list
list=[1, 3, 4, 5, 18, 12]
max=list[0]
second_largest=list[0]
for x in list:
    if x>max:
        second_largest=max
        max=x
    elif x>second_largest and x<max:
        second_largest=x
print(second_largest)
