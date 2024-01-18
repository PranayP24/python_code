#Remove duplicates from a list
my_list = [1,1,2,2,2,3,3,3,4,5,4,5,6,4,6,7,6,7]
result_list=[]
print('the original list:',my_list)
for i in my_list:
    if i not in result_list:
        result_list.append(i)
print("After remove the dupilcates:",result_list)