# Guilhem Vinet
# TECHNICAL TEST, 2022
# recruitment-test
# File description:
# range_sum fonction
#

def Calc (array, nb1, nb2):
    nb = 0

    if (nb1 <= 0):
        print("Invalid value of nb1 should >= 0")
        return (84)
    if (nb2 <= nb1):
        print("Invalid value of nb2 should >= nb2")
        return(84)
    if (len(array) < nb2):
        print("Invalid size of 'array', len of 'array' should be > nb2")
        return(84)
    for i in range (len(array)):
        if (array[i] >= nb1 and array[i] <= nb2):
            nb += array[i]
    return(nb)
