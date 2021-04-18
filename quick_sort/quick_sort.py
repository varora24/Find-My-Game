#!/usr/bin/env python3

def swap(first, second) :

    temp = first
    first = second
    second = temp

    
def partition(sort_dict, smallest, greatest, index, reverse=False) :

    partition = smallest
    left = smallest
    right = greatest

    if reverse :

        while 1 :

            while sort_dict[left][index] < sort_dict[partition][index] :         
                ++left
                if left == greatest :
                    break

            while sort_dict[partition][index] < sort_dict[right][index] :
                --right
                if right == smallest :
                    break

            if left >= right :
                break

            if sort_dict[left][index] >= sort_dict[right][index] :
                swap(sort_dict[left][index], sort_dict[right][index])

        if sort_dict[partition][index] >= sort_dict[right][index] :
            swap(sort_dict[partition][index], sort_dict[right][index])

    else :

        while 1 :
            while sort_dict[left][index] > sort_dict[partition][index] :         
                --left
                if left == greatest :
                    break

            while sort_dict[partition][index] > sort_dict[right][index] :
                ++right
                if right == smallest :
                    break

            if left <= right :
                break

            if sort_dict[left][index] <= sort_dict[right][index] :
                swap(sort_dict[left][index], sort_dict[right][index])

        if sort_dict[partition][index] <= sort_dict[right][index] :
            swap(sort_dict[partition][index], sort_dict[right][index])

        

    return right


def quick_sort(sort_dict, smallest, greatest, index, reverse=False) :

    if reverse :

        if len(sort_dict) == 0 or greatest <= smallest :
            return

        if greatest == (smallest + 1) :
            if sort_dict[smallest][index] > sort_dict[greatest][index] :
                swap(sort_dict[smallest], sort_dict[greatest])
            return

        part = partition(sort_dict, smallest, greatest, index)
        quick_sort(sort_dict, smallest, part - 1)
        quick_sort(sort_dict, part + 1, greatest)

    else :
        
        if len(sort_dict) == 0 or greatest >= smallest :
            return

        if smallest == (greatest - 1) :
            if sort_dict[smallest][index] < sort_dict[greatest][index] :
                swap(sort_dict[smallest], sort_dict[greatest])
            return

        part = partition(sort_dict, smallest, greatest, index)
        quick_sort(sort_dict, smallest, part - 1)
        quick_sort(sort_dict, part + 1, greatest)

    return sort_dict
