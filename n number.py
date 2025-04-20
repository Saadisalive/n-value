base = int(input("please enter your number :"))
exponent = int(input("please enter power number :"))
power = 1 
for i in range(1,exponent+1):
    power *= base
print(base,"power of",exponent,"=",power)