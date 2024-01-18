#Get the difference between two lists
lst1=[1, 2, 3, 4]
lst2=[1,2]
lst3=[]
for elements in lst1:
    if elements not in lst2:
        lst3.append(elements)
print(lst3)