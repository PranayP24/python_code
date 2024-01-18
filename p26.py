#Generate all permutations of a list
my_list=[1, 2, 3]
for i in range(len(my_list)):
    for j in range(len(my_list)):
            if i!=j:
                my_list[i],my_list[j]=my_list[j],my_list[i]
                print(my_list)
                my_list[i],my_list[j]=my_list[j],my_list[i]




