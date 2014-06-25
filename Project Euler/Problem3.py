def isPrime(n):
    """"precondition n is a nonnegative integer
postcondition:  return True if n is prime and False otherwise."""
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


number = 600851475143
point = 1
while point < number:
    if number % point == 0:
        if isPrime(point) == True:
            print point
        point = point + 1
    else:
		point = point + 1