#Print a dictionary in table format
my_dict= {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
print("Id | Name | Age")
print("-"* 15)
for key, value in my_dict.items():
    print(f"{key} | {value[0]:<4} | {value[1]}")
