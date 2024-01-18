#Flatten a shallow list
lst=[['pranay','hemanth','run out'],['vijay','chinna'],['friends']]
res_lst=[]
for char in lst:
    for i in char:
        res_lst.append(i)
print(res_lst)

index_out=0
while index_out<len(lst):
    index_in=0
    while index_in<len(lst[index_out]):
        res_lst.append(lst[index_out][index_in])
        index_in+=1
    index_out+=1
print(res_lst)
