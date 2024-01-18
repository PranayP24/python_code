#Create a set from a list
input_list=[1, 2, 2, 3, 3, 3]
output_set=set()
for num in input_list:
    output_set.add(num)
print(output_set)
num=0
while num < len(input_list):
    output_set.add(input_list[num])
    num+=1
print(output_set)
