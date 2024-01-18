#print a list in reverse order
my_list = [1,2,3,4,5]
print('list before reverse:',my_list)
reverse_list =[]
for values in my_list:
    reverse_list=[values]+reverse_list
print('list after reverse:',reverse_list )
