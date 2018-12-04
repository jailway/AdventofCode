with open('04_input.txt', ) as f:
    lines = f.readlines()
    lines.sort()

    guard = None
    guardsmaps = dict()

    asleep = False
    timesleep = 0

    for l in lines:
        #month = int(l[6:8])
        #day = int(l[9:11])
        #hour = int(l[12:14])
        min = int(l[15:17])

        if l[19] == "G":
            guard = int(l[26:].split(" ", maxsplit=1)[0])
            asleep = False
            if guard not in guardsmaps:
                guardsmaps[guard] = [0 for x in range(60)]

        elif l[19] == "f":
            asleep = True
            timesleep = min

        elif l[19] == "w":
            asleep = False
            for i in range(timesleep, min):
                guardsmaps[guard][i] += 1

    sum_times = dict([(g, sum(m)) for g, m in guardsmaps.items()])
    guard = max(sum_times, key=sum_times.get)
    print("answer to strategy 1 is: " + str(guard * guardsmaps[guard].index(max(guardsmaps[guard]))))

    max_times = dict([(g, max(m)) for g, m in guardsmaps.items()])
    guard = max(max_times, key=max_times.get)
    print("answer to strategy 2 is: " + str(guard * guardsmaps[guard].index(max(guardsmaps[guard]))))

