#################################################
#
# Prime number calculator
# Saul Contreras (Suulcoder)
#
#   This code contains a function that can check
#   if a number is member of the set of prime numbers
#################################################

#is_prime
#   Type:           Boolean
#   Parameters:     number: Int
#   Description:    Check if number is prime
def is_prime(number):
    if number==0:                                       #By definition 0 is not divisible by itself
        return False
    for i in range (2, int(number/2)+1):                #number cannot be divisible by n bigger than number/2
        if(number % i == 0):                            #Check if number is divisible by i
            return False
    return True
