import math
import os
import sys

def count_sort_func(data,maxdata,index):
   maxdata +=1
   count_list = [0]*(maxdata)
   count_dict = [0]*len(data)
   print(count_dict)
   #print(count_list)
   for n in data:
      #print(n[index])
      #exit()
      count_list[n[index]] +=1 # count_list[n[index]] + 1

   i = 0
   for n in range(len(count_list)):
      #print(n)
      #exit()
      while(count_list[n]>0):
         data[i] = n
         i+=1
         count_list[n] -= 1
   print("Hi")
   print(list(data))

   return data


if __name__ == "__main__":
   main()


