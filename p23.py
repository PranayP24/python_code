#Create a list by concatenating a given list which range goes from 1 to n
given_list = ['p','q']
n = 3

new_list = []

for i in range(1, n + 1):
    for item in given_list:
        new_list.append(item + str(i))

print(new_list)
