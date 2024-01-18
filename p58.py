#Calculate the exponentiation of a number
base_number=int(input('enter  the base number:'))
exponent_number=int(input('enter the exponent number:'))
output_value=1
for i in range(exponent_number):
    output_value=base_number**exponent_number
print(output_value)
i=0
while i<exponent_number:
    output_value=base_number**exponent_number
    i+=1
print(output_value)
