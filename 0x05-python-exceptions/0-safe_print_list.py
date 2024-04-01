#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        my_list = []

    try:
        count = 0
        for i in range(x):
            result = my_list[i]
            print("{}".format(result), end = "")
            count += 1
    except IndexError:
        pass
    print("")
    return(count)
