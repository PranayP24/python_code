#Print the Fibonacci sequence up to n terms
fibo_number=int(input('enter the how many terms:'))
fibonac=[0,1]
for num in range(2,fibo_number+1):
    fibonac.append(fibonac[num-1]+fibonac[num-2])
print(fibonac)

