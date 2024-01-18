#Convert a list into a nested dictionary of keys
input_list=[1,2,3,4]
out_dict={}
for i in range(len(input_list)):
    sub_dict={input_list[i]}
    out_dict[input_list[i]]=sub_dict
print(out_dict)
while input_list:
    value=input_list[0]
    input_list=input_list[1:]
    out_dict={value:out_dict}
print(out_dict)
