#Sort a list alphabetically in a dictionary
my_dict={'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']}
for key in my_dict:
    my_dict[key]=sorted(my_dict[key])
print(my_dict)
my_dict={'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']}
for key in my_dict:
    i = 0
    while i < len(my_dict[key])-1:
        j = 0
        while j < len(my_dict[key])-i-1:
            if my_dict[key][j] > my_dict[key][j+1]:
                # Swap if the elements are in the wrong order
                my_dict[key][j], my_dict[key][j+1] = my_dict[key][j+1], my_dict[key][j]
            j += 1
        i += 1
print(my_dict)