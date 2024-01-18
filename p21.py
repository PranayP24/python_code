#Check whether two lists are circularly identical
list1=[1,2,3,4]
list2=[2,4,3,1]
index=0
for x in range(len(list1)):
    z=0
    for y in range(len(list2)):
        