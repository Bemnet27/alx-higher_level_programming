#!/usr/bin/python3
def copy_list(my_list):
    new_list = []
    if my_list:
        for i in range(len(my_list)):
            new_list.append(my_list[i])
        return new_list


def new_in_list(my_list, idx, element):
    if my_list:
        _copy = copy_list(my_list)
        if idx < 0 or idx > len(my_list):
            return 'None'
        else:
            _copy[idx] = element
            return _copy
