from __future__ import print_function, division
def merge_sort_and_count_inversions(alist):
    '''Sorts the input list of integers "alist" and counts the number of 
    inversions. A inversion is defined as i < j | a[i] > a[j].
    Returns the number of inversions. Time complexity: O(nlog(n)).'''

    def merge_and_increment_inversions(aux_list, alist, lo, mid, hi):
        '''Merge two inputs sorted input lists and increments the number of
        inversions.'''
        for i in xrange(lo, hi+1):
            aux_list[i] = alist[i]

        le_ind = lo
        ri_ind = mid+1
        for index in xrange(lo, hi+1):
            if le_ind > mid:
                alist[index] = aux_list[ri_ind]
                ri_ind += 1
            elif ri_ind > hi:
                alist[index] = aux_list[le_ind]
                le_ind += 1

            elif aux_list[le_ind] < aux_list[ri_ind]:
                alist[index] = aux_list[le_ind]
                le_ind += 1
            else:
                alist[index] = aux_list[ri_ind]
                ri_ind += 1
                # Found inversion. All elements to the left are also inversions
                # since the left sub-list is sorted.
                li_n_inversions[0] += (mid+1) - le_ind

    def _sort(aux_list, alist, lo, hi):
        '''Divide the list into two halves and recursively sorts and counts
        the number of inversions between the two halves. The two halves are 
        merged into one sorted list.'''
        mid = lo + (hi-lo) // 2
        if hi <= lo: return None

        _sort(aux_list, alist, lo, mid)
        _sort(aux_list, alist, mid+1, hi)
        merge_and_increment_inversions(aux_list, alist, lo, mid, hi)
   

    li_n_inversions = [0] # Need scope-reach to sub-methods
    aux_list = [it for it in alist]
    _sort(aux_list, alist, 0, len(alist)-1)
    return li_n_inversions[0]
