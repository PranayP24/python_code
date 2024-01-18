#Create a dictionary from two lists
test_keys =['a','b','c']
test_values=[1,2,3]
my_dict={}
for index in range(len(test_keys)):
      my_dict[test_keys[index]]=test_values[index]
print(my_dict)