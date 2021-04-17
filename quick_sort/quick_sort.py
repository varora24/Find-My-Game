#!/usr/bin/env python3

def swap(first, second) :

    temp = first
    first = second
    second = temp

    
def partition(sort_dict, smallest, greatest) :

    partition = smallest
    left = smallest
    right = greatest

    while 1 :
        while sort_dict[left] < sort_dict[partition] :         
            ++left
            if left == greatest :
                break

        while sort_dict[partition] < sort_dict[right] :
            --right
            if right == smallest :
                break

        if left >= right :
            break

        if sort_dict[left] >= sort_dict[right] :
            swap(sort_dict[left], sort_dict[right])

    if sort_dict[partition] >= sort_dict[right] :
        swap(sort_dict[partition], sort_dict[right])

    return right


def quick_sort(sort_dict, smallest, greatest) :

    if len(sort_dict) == 0 or greatest <= smallest :
        return

    if greatest == (smallest + 1) :
        if sort_dict[smallest] > sort_dict[greatest] :
            swap(sort_dict[smallest], sort_dict[greatest])
        return

    part = partition(sort_dict, smallest, greatest)
    quick_sort(sort_dict, smallest, part - 1)
    quick_sort(sort_dict, part + 1, greatest)

    return sort_dict
