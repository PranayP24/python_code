#Check if an element exists in a tuple
my_tuple=(1, 2, 3, 4)
element_To_check=3
element_exists=False
for item in my_tuple:
    if item ==element_To_check:
       element_exists=True
       break
print(element_exists)
item = 0
while item < len(my_tuple):
    if item == element_To_check:
        element_exists=True
        break
    item+=1
print(element_exists)
