# #Print a specified list after removing the 0th, 4th, and 5th elements
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color_r=[]
print('original list :',color)
for i in range(len(color)):
    if i==0:
        continue
    elif i==4:
        continue
    elif i==5:
        continue
    color_r.append(color[i])
print('after removing the color :',color_r)

print('Original list:', color)

for i in range(len(color)):
    if i == 0 or i == 4 or i == 5:
        continue
    color_r.append(color[i])

print('After removing elements at specific indices:', color_r)

