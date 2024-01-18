#Find the index of an item in a specified list
my_list=[1, 2, 3, 4, 5]
#print('indices and values in the list:')
for i in range(len(my_list)):
    val=my_list[i]
    #print((i,val))
    if val==4:
        print(i)
my_list=['hello','red','yellow','tube','white']
#print('indices and values in the list:')
for i in range(len(my_list)):
    val=my_list[i]
    #print((i,val))
    if val=='red':
        print(i)
