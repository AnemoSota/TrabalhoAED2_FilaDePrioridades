

def trocavel(i, j):
    t = True

    if (i - j == 1) and (i % 3 == 0) :
        t = False
    if (i - j == -1) and (i % 3 == 2):
        t = False
    if (i - j == 3) and (i < 3):
        t = False
    if (i - j == -3) and (i > 5):
        t = False

    return t