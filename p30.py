#Flatten a list without using recursion
lst=[[1, 2], [3, 4], [5, 6]]
res_lst=[]
for char in lst:
    for i in char:
        res_lst.append(i)
print(res_lst)
