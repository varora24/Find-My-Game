#!/usr/bin/env python3

def swap(first, second) :

    temp = first
    first = second
    second = temp

    
def partition(sort_vec, smallest, greatest) :

    partition = smallest
    left = smallest
    right = greatest

    while 1 :
        while sort_vec[left] < sort_vec[partition] :         
            ++left
            if left == greatest :
                break

        while sort_vec[partition] < sort_vec[right] :
            --right
            if right == smallest :
                break

        if left >= right :
            break

        if sort_vec[left] >= sort_vec[right] :
            swap(sort_vec[left], sort_vec[right])

    if sort_vec[partition] >= sort_vec[right] :
        swap(sort_vec[partition], sort_vec[right])

    return right


def quick_sort(sort_vec, smallest, greatest) :

    if len(sort_vec) == 0 or greatest <= smallest :
        return

    if greatest == (smallest + 1) :
        if sort_vec[smallest] > sort_vec[greatest] :
            swap(sort_vec[smallest], sort_vec[greatest])
        return

    part = partition(sort_vec, smallest, greatest)
    quick_sort(sort_vec, smallest, part - 1)
    quick_sort(sort_vec, part + 1, greatest)
