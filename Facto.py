#Owner: Overrideveloper
#Description: Factorial Program
from memory_profiler import memory_usage

from datetime import datetime
startTime = datetime.now()
x = 0
for x in range(x,4):

    def factorial(n): 

        if n == 0: 
            return 1 
        
        elif n<0:
            print("There is no factorial for this number")
    
        else: 
            return n * factorial(n-1)
        
    number = int(input("Enter the number: "))
    output = factorial(number)
    print(output)

print ("The execution time is ",(datetime.now()- startTime))

mem_usage = memory_usage(factorial)

print('Memory usage (in chunks of .1 seconds): %s'% mem_usage)

print('Maximum memory usage: %s'% max(mem_usage))
