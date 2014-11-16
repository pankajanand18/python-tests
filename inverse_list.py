test_case = int(raw_input())

while test_case > 0:
    length = int(raw_input())
    index = 1
    input_data = raw_input()
    list = []
    original_list = []
    counter = 0
    input_data = input_data.split(' ')
    print input_data
    for data in input_data:
        data = int(data)
        list.append(data)
        original_list.insert(data - 1, counter + 1)
        counter = counter + 1

    if cmp(list, original_list) == 0:
        print "inverse"
    else:
        print "not inverse"

    test_case = test_case - 1