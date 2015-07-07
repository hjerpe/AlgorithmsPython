import math

def count_inversions_and_sort(alist):
    '''Sorts the list of integers "alist" and counts the number of inversions. 
    A inversion is defined as i < j | a[i] > a[j].
    Returns a tuple containing (#inversions, [sorted list]).
    Time complexity: nlog(n).'''
    # Base case
    if len(alist) == 1:
        return (0, alist)
    else:
        ind_middle = int(math.ceil(len(alist)/2))

        (count_left, li_left) = count_inversions_and_sort(alist[:ind_middle])
        (count_right, li_right) = count_inversions_and_sort(alist[ind_middle:])

        (count_middle, sorted_list) = merge_and_count_inversions(li_left, 
            li_right)

    return (count_left + count_right + count_middle, sorted_list)
    

def merge_and_count_inversions(list1, list2):
    '''Merge two sorted lists into one sorted list and counts the number of
    mid inversions. A  mid inversion is defined as i < j | a[i] > a[j]
    where i is a index in list1 and j is a index in list2.
    Returns a tuple containing (#mid_inversions, [sorted list]).'''
    len_op = len(list1) + len(list2)
    sorted_list = [0 for _ in xrange(len_op)]
    ind_sorted = 0
    ind1, ind2 = 0, 0
    n_inversions = 0

    while ind_sorted < len_op:
        if list1[ind1] < list2[ind2]:
            sorted_list[ind_sorted] = list1[ind1]
            ind1 += 1
        else:
            sorted_list[ind_sorted] = list2[ind2]
            ind2 += 1

            n_inversions += len(list1) - ind1
        ind_sorted += 1

        # If smaller list already inserted
        if ind1 == len(list1):

            for i in xrange(ind2, len(list2)):
                sorted_list[ind_sorted] = list2[i]
                ind_sorted += 1
        elif ind2 == len(list2):

            for i in xrange(ind1, len(list1)):
                sorted_list[ind_sorted] = list1[i]
                ind_sorted += 1
    return (n_inversions, sorted_list)
