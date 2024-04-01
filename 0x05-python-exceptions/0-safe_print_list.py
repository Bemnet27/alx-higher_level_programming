#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        my_list = []

    try:
        count = 0
        for i in range(0, x):
            result = my_list[i]
            print(result)
            count += 1
    except IndexError as e:
        print(e)
        return(count)
    except TypeError as e:
        print(e)
