# Guilhem Vinet
# TECHNICAL TEST, 2022
# recruitment-test
# File description:
# ComputeJoinPoint fonction
#

def ComputeJoinPoint(s1, s2):
    str_s1 = str(s1)
    str_s2 = str(s2)
    temp_s1 = s1
    temp_s2 = s2
    nb = 0

    while (temp_s1 != temp_s2 and (temp_s1 and temp_s2) < 20000000):
        if (temp_s1 > temp_s2):
            for i in range (len(str_s2)):
                nb = int(str_s2[i])
                temp_s2 += nb
            str_s2 = str(temp_s2)
        for i in range (len(str_s1)):
            nb = int(str_s1[i])
            temp_s1 += nb
        str_s1 = str(temp_s1)
    if (0 < temp_s1 < 20000000):
        return(temp_s1)
    return(-1)
