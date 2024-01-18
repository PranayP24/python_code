#Get unique values from a list
values=[1,2,2,3,3,3,4,4,5,6,5]
unique_values=set(values)
print(unique_values)
unique_values=[]
for i in values:
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)
