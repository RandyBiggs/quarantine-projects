# Given an input of a list and an index, return the same list without the specified index
# AKA Didn't have an idea for today


def remove_element(lst, idx):
    ret_lst = []

    # Index is beyond the given list
    if idx > len(lst):
        print("Index Out of Bounds")
        ret_lst = -1
    # Index is negative, i.e. end of list indexing
    elif idx < 0:
        ret_lst = lst[0:idx]
    # Expected use-case
    else:
        for i in range(len(lst)):
            if i == idx:
                continue
            else:
                ret_lst.append(lst[i])
    print(ret_lst)
    return ret_lst


# Test
remove_element([1, 2, 3, 4, 5], 0)
