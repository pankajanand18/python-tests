from itertools import izip


def printRange(birth_event, death):
    birth_event.sort()
    death.sort()
    b = 0
    d = 0

    count = 0
    max_count = 0
    start_date = birth_event[0]
    end_date = 0

    while b < len(birth_event) and d < len(death):
        if birth_event[b] < death[d]:
            count = count + 1
            b += 1
            if count > max_count:
                start_date = birth_event[b - 1]
                max_count = count
        else:
            print 'death'
            if count == max_count:
                end_date = death[d]
            count = -1
            d += 1

    print birth_event

    print death
    print max_count
    print start_date
    print end_date


printRange([5, 6, 2], [10, 15, 7])