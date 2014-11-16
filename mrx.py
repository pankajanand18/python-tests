def getIntegerInput():
    inputs = raw_input()
    input_int_list = [int(i) for i in inputs.split(' ')]

        # print input_int_list
    return input_int_list


def solve(input_list, index, result_store, k):
    if index >= len(input_list):
        return 0
    if result_store[index] is not -1:
        return result_store[index]
    ret = max(-500000, solve(input_list, index + 1, result_store, k))
    ret = max(ret, input_list[index] + solve(input_list, index + k + 1, result_store, k))
    result_store[index] = ret
    return ret


def getCalculateMaxTime(list, k):
    length = len(list)
    result_store = [0] * len(list)

    result_store[0] = max(list[0], list[1])

    for i in xrange(2, len(list)):
        life = list[i]

        if life < 0:
            result_store[i] = result_store[i - 1]
        elif i - k - 1 < 0:
            result_store[i] = max(result_store[i - 1], list[i])
        else:
            # print i-k-1
            result_store[i] = max(result_store[i - 1], list[i] + result_store[i - k - 1])
    print result_store[-1]


t = input()
list_of_input = []
for i in xrange(t):
    inputs = getIntegerInput()
    array_size = inputs[0]
    k = inputs[1]
    input_array = getIntegerInput()
    list_of_input.append((input_array, k))

for i in list_of_input:
    try:
        input_list = i[0]
        k = i[1]
        result_store = [-1] * len(input_list)
        print solve(input_list, 0, result_store, k)
    except Exception, e:
        print 'exception came %s' % e
        pass
	


	

	

			





