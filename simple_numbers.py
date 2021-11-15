def simple_numbers(bound):
    simple = True
    for i in range(1, bound):
        for j in range(2, i):
            if not i % j and i != j: simple = False
        if simple:
            yield i
        simple = True

simp = simple_numbers(10)

for i in simp:
    print(i)
