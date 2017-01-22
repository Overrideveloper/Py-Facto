#Owner: Overrideveloper
#Description: Factorial Program

from datetime import datetime
import os
import psutil

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

process = psutil.Process(os.getpid())

print ("The execution time is ",(datetime.now()- startTime))

print("Memory consumption in Kilobytes is: ")
print(process.memory_info().rss / 1024)
