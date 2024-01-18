#Perform integer division and find the remainder
dividend_value=int(input('enter the dividend value:'))
divisor_value=int(input('enter the divisor value :'))
quotient=0
remainder=1
for num in range(dividend_value):
    quotient= dividend_value// divisor_value
    remainder=dividend_value% divisor_value
print('integer division:',quotient,'remainder:',remainder)
num =0
while num < dividend_value:
    quotient= dividend_value// divisor_value
    remainder=dividend_value% divisor_value
    num+=1
print('integer division:',quotient,'remainder:',remainder)
