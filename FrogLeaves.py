
def soln(x, a):
    possible = []
    for i, dig in enumerate(a):
        if dig == x:
            possible.append(a[:i + 1])

    fil = []
    for part in possible:
        index = 0
        for dig in range(1, x + 1):
            if dig not in part:
                index = 0
            else:
                index += 1
        fil.append([index, part])

    val = -1
    for group in fil:
        if group[0] == x:
            listy = group[1]
            val = len(listy) - 1
            break
    return val


print(soln(5, [1, 3, 1, 4, 2, 3, 5, 4, 5]))
