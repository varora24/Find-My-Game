#!/usr/bin/env python3

def swap(smallest, greatest) :

    temp = smallest
    smallest = greatest
    greatest = temp
        

def partition(sort_dict, smallest, greatest, index, reverse=False) :

    partition = smallest
    left = smallest + 1
    right = greatest

    count = 0

    while 1 :
        while int(sort_dict[left][index]) < int(sort_dict[partition][index]) :
            left += 1
            if left == greatest :
                break
        while int(sort_dict[partition][index]) < int(sort_dict[right][index]) :
            right -= 1
            if right == smallest :
                break
        if left >= right :
            break
        elif int(sort_dict[left][index]) > int(sort_dict[right][index]) :
            swap(sort_dict[left], sort_dict[right])
            break


    if int(sort_dict[partition][index]) > int(sort_dict[right][index]) :
        swap(sort_dict[partition], sort_dict[right])

    #else :

      #  while 1 :
     #       while sort_dict[left][index] > sort_dict[partition][index] :         
        #        --left
       #         if left == greatest :
         #           break

          #  while sort_dict[partition][index] > sort_dict[right][index] :
           #     ++right
            #    if right == smallest :
             #       break

          #  if left <= right :
           #     break

          #  if sort_dict[left][index] <= sort_dict[right][index] :
           #     swap(sort_dict[left][index], sort_dict[right][index])

        #if sort_dict[partition][index] <= sort_dict[right][index] :
         #   swap(sort_dict[partition][index], sort_dict[right][index])

        

    return right



def quick_sort_func(sort_dict, smallest, greatest, index, reverse=False) :

    #if not reverse :

    if len(sort_dict) == 0 or greatest <= smallest :
        return

    if greatest == (smallest + 1) :
        if int(sort_dict[smallest][index]) > int(sort_dict[greatest][index]) :
            swap(sort_dict[smallest], sort_dict[greatest])
        return


    part = partition(sort_dict, smallest, greatest, index)
    quick_sort_func(sort_dict, smallest, part - 1, index)
    quick_sort_func(sort_dict, part + 1, greatest, index)

 #   else :
  #      
   #     if len(sort_dict) == 0 or greatest >= smallest :
    #        return

     #   if smallest == (greatest - 1) :
      #      if sort_dict[smallest][index] < sort_dict[greatest][index] :
       #         swap(sort_dict[smallest], sort_dict[greatest])
        #    return

        #part = partition(sort_dict, smallest, greatest, index, reverse)
        #quick_sort(sort_dict, smallest, part - 1)
        #quick_sort(sort_dict, part + 1, greatest)
