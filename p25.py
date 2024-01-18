#Check whether a list contains a sublist
list= [2, 4, 3, 5, 7]
sub_list=[4, 3]
result=False
for i in range(len(list)-len(sub_list)+1):
    if list[i:i+len(sub_list)]==sub_list:
        result=True
        print(result)
        break
i=0
while i <= (len(list)-len(sub_list)+1):
    if list[i:i+len(sub_list)]==sub_list:
        result=True
        print(result)
        break
    i+=1
