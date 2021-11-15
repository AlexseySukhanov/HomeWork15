def geometric_progression(mult, amount):
    i = 1
    count = 0
    stop = False
    while not stop and count < amount:
        stop = yield i
        i = i * mult
        count += 1

geom = geometric_progression(3,10)

count = 1
bound = None
for i in geom:
    print(i)
    if count == bound:
        geom.send(True)
    count += 1