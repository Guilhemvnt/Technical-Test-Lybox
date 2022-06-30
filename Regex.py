# Guilhem Vinet
# TECHNICAL TEST, 2022
# recruitment-test
# File description:
# ExtractRent fonction
#

def ExtractRent(content):
    numbers = ([int(s) for s in re.findall(r'-?\d+\.?\d*', content)])
    numbers.sort()
    array = content.split()

    for i in range (len(array)):
        if array[i].find("an") > 0 or array[i] == "an":
            return (numbers[len(numbers) - 1])
    return(numbers[len(numbers) - 1] * 12)
