import pb1, random

def problem2(x=1.0):
    y = pb1.findSmallestU()
    z = pb1.findSmallestU()

    print 'Adunarea este asociativa pentru parametrii specificati:', (x + y) + z == x + (y + z)
    x = random.random()
    y = random.random()
    while (x * y) * z == x * (y * z):
        x = random.random()
        y = random.random()

    print 'Numerele pentru care inmultirea nu este ascociativa sunt:'
    print x, y, z

problem2()
