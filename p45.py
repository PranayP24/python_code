#List slicing
input_list=[1,2,3,4,5]
start_index, end_index=2,4
output_list=[]
for i in range(start_index,end_index):
    output_list.append(input_list[i])
print(output_list)
index=start_index
while index<end_index:
    output_list.append(input_list[index])
    index+=1
print(output_list)
