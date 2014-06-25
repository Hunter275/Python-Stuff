number = 1
point = 1
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

while point <= 10001:
    if isPrime(number) == True:
        print str(number) + " " + str(point)
        number = number + 1
        point = point + 1
    else:
        #print "nothin"
        number = number + 1
        #point = point + 1