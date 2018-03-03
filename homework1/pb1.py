


def findSmallestU():
    lastU = 0
    u = 0.1
    while 1 + u != 1:
        lastU = u
        u *= 0.1

    return lastU

print findSmallestU()
