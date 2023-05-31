#################################################
#
# Saul Contreras (Suulcoder)
#
#   This code calculates the sum of consecutive 
#   numbers until N.
#################################################

#sum_of_consecutive_numbers
#   Type:           Int
#   Parameters:     n: Int
#   Description:    Get the sum of consecutive numbers
def sum_of_consecutive_numbers(n):
    if n==1:
        return 1
    else:
        return sum_of_consecutive_numbers(n-1)+n