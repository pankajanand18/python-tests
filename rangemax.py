def getMax(list):
    max = list[0]
    for item in list:
        if item > max:
            max = item

    return max


def printRange(start_list, end_list):
    max = getMax(end_list)

    count_array = [0] * max;
    for i in xrange(len(start_list)):
        for item in xrange(start_list[i] - 1, end_list[i]):
            count_array[item] = count_array[item] + 1

    max_age = count_array[0]
    max_age_index = []
    print count_array
    for item in xrange(len(count_array)):

        if count_array[item] > max_age:
            max_age = count_array[item]
            max_age_index = [item + 1]
        elif max_age == count_array[item]:
            max_age_index.append(item + 1)

    print max_age_index


printRange([5, 6, 2], [10, 15, 7])

