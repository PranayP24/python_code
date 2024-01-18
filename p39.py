#Remove spaces from dictionary keys
my_dict={"a b": 1, "c d": 2, "e f": 3}
new_dict={}
for key,values in my_dict.items():
    new_key=key.replace(' ','')
    new_dict[new_key]=values
print(new_dict)
keys_to_process=list(my_dict.keys())
i=0
while i < len(keys_to_process):
    key = keys_to_process[i]
    new_key=key.replace(' ','')
    new_dict[new_key]=my_dict[key]
    i+=1
print(new_dict)
