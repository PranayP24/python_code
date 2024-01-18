#Concatenate two lists
list1 = [1,2,3,4]
list2 =[5,6,7,8]
print('list1 before concatenation:',list1)
for i in list2:
    list1+=list2
    break
print('list1 after concatenation:',list1)