#Create a dictionary from a string
mystr='python Advanced To Go'
mydict=dict()
for char in mystr:
    if char in mydict:
        mydict[char]+=1
    else:
        mydict[char]=1
print(mydict)
index=0
while index<len(mystr):
     char=mystr[index]
     if char not in mydict:
         mydict[char]=1
     else:
        mydict[char]+=1
     index+=1
print(mydict)