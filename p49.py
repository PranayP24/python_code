#Count occurrences of an element in a lis
my_list=[1, 4, 2, 4, 5, 4, 1]
element_To_count=4
count=0
for num in my_list:
    if num==element_To_count:
        count+=1
print(count)
num = 0
while num < len(my_list):
    if my_list[num]==element_To_count:
        count+=1
    num+=1
print(count)
