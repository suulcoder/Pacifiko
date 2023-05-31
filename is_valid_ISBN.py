#################################################
#
# Saul Contreras (Suulcoder)
#
#   This code checks if ISBN is valid
#################################################

#is_a_valid_ISBN
#   Type:           Boolean
#   Parameters:     ISBN: String
#   Description:    Check if ISBN is valid
def is_a_valid_ISBN(ISBN):
    if (len(ISBN)==10):
        control_list = ([int(character)*(index+1) for index,character in enumerate(ISBN[0:9])])         #Multiply each digit with its index
        control_digit = sum(control_list)%11                                                            #Get control digit
        if(control_digit==ISBN[9]):                                                                     #If control digit is lower than 10
            return True
        elif(control_digit==10 and ISBN[9]=='X'):                                                       #If control digit is 10
            return True
    return False