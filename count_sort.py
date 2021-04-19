import math
import os
import sys
import pprint

def count_sort_func(data,maxdata,index):
   maxdata +=1
   count_list = [0]*(maxdata)
   count_dict = data
   #print(count_dict)
   #print(count_list)
   for n in data:
      
      count_list[n[index]] +=1 # count_list[n[index]] + 1

   i = 0
   count = 0
   for n in range(len(count_list)):
      #print(n)
      #exit()
      while(count_list[n]>0):
         for vals in count_dict:
            j = 0
            if vals[index]==n:
               pprint.pprint(vals)
               count+=1
               print(count)
               data[i] = vals
               count_dict.pop(j)
            j+=1
         #data[i] = n
         i+=1
         count_list[n] -= 1
   #pprint(list(data))

   return data

