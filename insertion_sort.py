#welcome to the insertion sort algorithm! 

#i have written the script in python, and this sorting algorithm has a complexity of O (n + f (n)) where f (n) is inversion count.
#defining the algorithm and giving it a paramter of list_a
def insertion_sort(list_a):
  #specifying the range, note that we use 1 instead of 0 #because the 1st number will always be in the sorted list, #but we still do sort all the numbers, including the #number in the zeroth position
  indexing_length = range(1,len(list_a))
  #read the below line as - "for every value in #indexing_length"
  for i in indexing_length:
    value_to_sort = list_a[i]
    #now, we actually want to reverse the values of i
    while list_a[i-1] > value_to_sort and i > 0:
      list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
      #here, we are moving the index one step ahead
      i -= 1
    # now we simply return the list after the while loop is over, because we dont wanna have the entire procedure shown
  return list_a
#finally, we print out the function 
print(insertion_sort([1,6, 7, 4, 7,8, 9, 3, 2, 8]))
