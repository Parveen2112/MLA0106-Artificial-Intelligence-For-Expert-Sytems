def water_jug():
    a, b = 0, 0  # start with empty jugs
    A, B = 4, 3  # capacities

    steps = []
    while a != 2:
        if a == 0:
            a = A  # fill 4-gallon
        elif b == B:
            b = 0  # empty 3-gallon
        else:
            pour = min(a, B - b)
            a -= pour
            b += pour
        steps.append((a, b))
    
    print("Steps to get 2 gallons in 4-gallon jug:")
    for s in steps:
        print(s)

water_jug()
