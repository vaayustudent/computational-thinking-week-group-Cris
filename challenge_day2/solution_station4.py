#Time 09:43:50 SI:15 SO:False I:2075
#Time 09:44:01 SI:83 SO:True I:5822
# prime numbers

def solution_station4(x):
    if x == 0 or x == 1:
        return False
    elif x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True
    else:
        return False

print(solution_station4(7))