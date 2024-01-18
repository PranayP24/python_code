#Find the second smallest number in a list
list=[5,9,8,2,0,4,7]
smallest=min(list[0],list[1])
second_smallest_number=max(list[0],list[1])
for x in list:
    if x<smallest:
        second_smallest_number=smallest
        smallest=x
    elif x<second_smallest_number and x!=smallest:
        second_smallest_number=x
print(second_smallest_number)