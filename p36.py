#Count the values associated with a key in a dictionary
test_dict={'A': [1, 2, 3], 'B': [4, 5], 'C': [6]}
result_dict={}
for key,values in test_dict.items():
    count=len(values)
    result_dict[key]=count
print(result_dict)
keys=list(test_dict.keys())
index=0
while index<len(keys):
    key=keys[index]
    values=test_dict[key]
    count=len(values)
    result_dict[key]=count
    index+=1
print(result_dict)
