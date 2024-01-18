#Find the number of elements in a list.
my_list = [1,2,3,4,5]
size=0
for i in my_list:
    size+=1
print(size)
i=0
while i < len(my_list):
    size+=1
    i+=1
print(size)