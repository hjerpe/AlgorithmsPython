from __future__ import print_function, division
import numpy as np
# Investigate how the number of comparisons used by quick-sort changes for
# under different pivoting selection strategies.

def quick_sort(alist):
    '''Sorts the the input list and outputs the total number of comparisons.'''
    
    def pivot_selection(alist, l_index, r_index, int_piv_strategy):
        '''Returns an index for the input list alist, j used s.t. all numbers 
        are partitioned into two parts consisting of all numbers smaller than
        A[j] and all numbers larger than A[j].'''
        if int_piv_strategy == 1:
            return l_index

    def partitioning(alist, left_index, end_index):
        '''Partitions the input list between the indices left_index, right_index
        around a pivot p such that all numbers to the left of p is smaller and 
        all number to the right are larger. Returns the index to the pivoting
        element.'''
        int_piv_strategy = 1
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
        '''Recursicely sorts the input list using divide and conquer paradigm 
        and increments the number of comparisons done by the method partitioning.
        '''
        if len(alist) != 1:
            
            split_index = partitioning(alist, left_index, end_index)
            n_comparisons[0] += end_index - (left_index+1)

            if left_index+1 < split_index: 
                recursive_sort(alist, left_index, split_index)

            if split_index+1 < end_index:
                recursive_sort(alist, split_index+1, end_index)
   

    # Sorts the input array and returns the number of comparisons.
    n_comparisons = [0]
    if len(alist) == 1: return n_comparisons
    recursive_sort(alist, 0, len(alist))

    return n_comparisons[0]

n = 9
random_list = np.unique(np.random.random_integers(0, 100, n))
np.random.shuffle(random_list)
# error_list = [51, 14, 80, 55]
# error_list = [10, 34, 89, 49, 11, 38, 0, 15, 39]
org_list = random_list
# org_list = error_list
org_list = [8, 10, 1, 9, 7, 2, 6, 3, 5, 4]
print('org list {l}'.format(l=org_list))
sorted_list = quick_sort(org_list)
print('sorted_list: {s}'.format(s=sorted_list))

print('org list after call: {o}'.format(o=org_list))
