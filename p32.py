#Find the highest 3 values in a dictionary
my_dict= {'a': 10, 'b': 15, 'c': 4, 'd': 25, 'e': 8}
max_values={}
for values in my_dict.values():
    for i in range(3):
        if values > max_values[i]:
            max_values[i+1:]=max_values[i:2]
            max_values[i]=values
            break
print(max_values)
