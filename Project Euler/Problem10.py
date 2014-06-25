def isPrime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:
         # return False
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

point = 1
number = 1
numsum = 0
while point <= 2000000:
    if isPrime(number) == True:
        numsum = numsum + number
        number = number + 1
        point = point + 1
    else:
        number = number + 1
        point = point + 1
print numsum
