#Find the list of words that are longer than n from a given list of words
lst= ['hello', 'world', 'name', 'python', 'programming']
lst2=[]
n=4
for i in range(len(lst)):
    temp=lst[i]
    if len(temp)>n:
       lst2.append(lst[i])
print(lst2)
