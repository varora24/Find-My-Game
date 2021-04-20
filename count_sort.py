import math
import os
import sys
import pprint

def count_sort_func(data,maxdata,index):
   maxdata +=1
   count_list = [0]*(maxdata)
   count_dict = data
   for n in data:
      count_list[n[index]] +=1

   i = 0
   count = 0
   for n in range(len(count_list)):
      print(n)
      while(count_list[n]>0):
         for vals in count_dict:
            j = 0
            if vals[index]==n:
               #pprint.pprint(vals)
               pprint.pprint(count_dict)
               print("---------------------------------")
               data[i] = vals
               count+=1
               print(count)
               count_dict.pop(j)
               break
            j+=1
         #data[i] = n
         i+=1
         print("Hi")
         count_list[n] -= 1
   #pprint(list(data))
   return data

