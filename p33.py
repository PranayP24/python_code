#Combine values in a Python list of dictionaries 
my_list=[{1: 10}, {2: 20}, {3: 30}]
combined_dict={}
for my_dict in my_list:
    for key,value in my_dict.items():
        if key not in combined_dict:
            combined_dict[key]=[value]
        else:
            combined_dict[key].append(value)
print(combined_dict)

index=0
while index<len(my_list):
    my_dict=my_list[index]
    for key,value in my_dict.items():
        if key not in combined_dict:
            combined_dict[key]=[value]
        else:
            combined_dict[key].append(value)
    index+=1
print(combined_dict)
