def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    if not (idx < 0 or idx > (len(my_list) - 1)):
        list_copy[idx] = element
    return list_copy
