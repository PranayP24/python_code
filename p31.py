#Create and display all combinations of letters, selecting each letter from a different key in
#a dictionary 
my_dict= {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = []
for char1 in my_dict['1']:
    for char2 in my_dict['2']:
        combination = char1 + char2 
        combinations.append(combination)
print(combinations)
char1=0
while char1 < len(my_dict['1']):
    char2=0
    while char2 < len(my_dict['2']):
        combination=my_dict['1'][char1]+my_dict['2'][char2]
        combinations.append(combination)
        char2+=1
    char1+=1
print(combinations)
