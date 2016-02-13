from __future__ import print_function, division
import math
# Investigate how the number of comparisons used by quick-sort changes under 
# different pivoting selection strategies.

def count_comparisons_and_sort(alist, int_piv_strategy):
    '''Sorts the input list and outputs the total number of comparisons using 
    the Quick-Sort algorithm.'''
    
    def pivot_selection(alist, l_index, r_index, int_piv_strategy):
        '''Returns an index for the input list alist, j used s.t. all numbers 
        are partitioned into two parts consisting of all numbers smaller than
        A[j] and all numbers larger than A[j].'''
        if int_piv_strategy == 1:
            return l_index
        elif int_piv_strategy == 2:
            return r_index-1
        elif int_piv_strategy == 3:
            # Returns the median of the start, middle and end numbers. The 
            # median of a list of length 2k is defined as the value at index k.
            head = alist[l_index]
            tail = alist[r_index-1]
            len_list = r_index - l_index

            mid_index = int(math.floor(len_list/2)) + l_index
            mid_index += -1 if len_list%2 == 0 else 0
            mid = alist[mid_index]
            sorted_indices = [y for x,y in sorted(zip([head, mid, tail], 
                [l_index, mid_index, r_index-1]))]
            return sorted_indices[1]

    def partitioning(alist, left_index, end_index):
        '''Partitions the input list between the indices left_index, right_index
        around a pivot p such that all numbers to the left of p is smaller and 
        all number to the right are larger. Returns the index to the pivoting
        element.'''
        int_piv_strategy = piv_strategy[0]
        pivot_index = pivot_selection(alist, left_index, end_index, 
                int_piv_strategy)
        alist[left_index], alist[pivot_index] = \
                alist[pivot_index], alist[left_index]

        pivot = alist[left_index]

        # Find split_index s.t. a[i] < p for all i < split_index
        split_index = left_index + 1
        for j in xrange(left_index+1, end_index):
            if alist[j] < pivot:
                alist[split_index], alist[j] = alist[j], alist[split_index]
                split_index += 1
        # Swap pivot and return the index that splits the remaining left and 
        # right subproblems
        alist[left_index], alist[split_index-1] = \
                alist[split_index-1], alist[left_index]
        return split_index-1

    def recursive_sort(alist, left_index, end_index):
        '''Recursicely sorts the input list between the indices 
        [left_index, end_index) using divide and conquer paradigm and increments 
        the number of comparisons done by the partitioning method.'''
        if end_index - left_index > 1:
            
            split_index = partitioning(alist, left_index, end_index)
            n_comparisons[0] += end_index - (left_index+1)

            if left_index+1 < split_index: 
                recursive_sort(alist, left_index, split_index)

            if split_index+1 < end_index:
                recursive_sort(alist, split_index+1, end_index)
   

    # Sorts the input array and returns the number of comparisons.
    piv_strategy = [int_piv_strategy]
    n_comparisons = [0]
    if len(alist) == 1: return n_comparisons
    recursive_sort(alist, 0, len(alist))
    return n_comparisons[0]


# filename = 'Data/test_10.txt'
# filename = 'Data/test_100.txt'
# filename = 'Data/test_1000.txt'
# f = open(filename, 'r')
# li_integers = [int(line.rstrip('\n')) for line in f]

# f.close()
li_integers =  [ 7, 5, 1, 4, 8, 3, 10, 2, 6, 9 ]
counts = lambda int_strat: count_comparisons_and_sort(
        [x for x in li_integers], int_strat)
list_strategies = [1,2,3]
print(len(li_integers))
print(map(counts, list_strategies))
