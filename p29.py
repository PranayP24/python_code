#Find the index of an item in a specified list
my_list=[1, 2, 3, 4, 5]
i=0
while i<len(my_list):
    if my_list[i]==4:
        print(i)
    i+=1

my_list=['hello','red','yellow','tube','white']
value=input('enter the value :')
i=0
while i<len(my_list):
    if my_list[i]==value:
        print(i)
    i+=1
