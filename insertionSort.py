from operator import length_hint


def insertion_sort(a_array):
    #the range between the start of the first element to compare or swap up to the length of a_array
    index_length = range(1,length_hint(a_array)) 

    for i in index_length: 
        value_to_sort = a_array[i]
        while a_array[i - 1] > value_to_sort and i>0:
            a_array[i], a_array[i - 1] = a_array[i -1], a_array[i] #swap
            i = i-1 #increment down the list
    return a_array

print(insertion_sort([8,56,1,5]))