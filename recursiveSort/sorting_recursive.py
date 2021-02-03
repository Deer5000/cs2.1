from random import randrange, shuffle



def merge(left, right):
    result = []
    while(left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop
        else:
            result.append(right[0])
            right.pop

    if left:
        result += left
    if right:
        result += right

    return result

    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n) because it merges n elements.
    TODO: Memory usage: O(n)"""
    # TODO: Repeat until one list is empty✅
    # TODO: Find minimum item in both lists and append it to new list✅
    # TODO: Append remaining items in non-empty list to new list✅

def merge_sort(items):
    if len(items) <= 1:
        return items
    
    mid_idx = len(items) // 2
    left_split = items[:mid_idx]
    right_split = items[mid_idx:]

    left_sort = merge_sort(left_split)
    right_sort = merge_sort(right_split)

    return merge(left_sort, right_sort)


    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(logn) because it firsts divides which is O(1) and then it conquers
    which recursively sorts the two subarrays of n/2 elements each.
    TODO: Memory usage: O(n)"""
    # TODO: Check if list is so small it's already sorted (base case) ✅
    # TODO: Split items list into approximately equal halves ✅
    # TODO: Sort each half by recursively calling merge sort ✅
    # TODO: Merge sorted halves into one list in sorted order ✅


# def partition(items, low, high):
#     """Return index `p` after in-place partitioning given items in range
#     `[low...high]` by choosing a pivot (TODO: document your method here) from
#     that range, moving pivot into index `p`, items less than pivot into range
#     `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Choose a pivot any way and document your method in docstring above
#     # TODO: Loop through all items in range [low...high]
#     # TODO: Move items less than pivot into front of range [low...p-1]
#     # TODO: Move items greater than pivot into back of range [p+1...high]
#     # TODO: Move pivot item into final position [p] and return index p


def quick_sort(list, start, end):
  if start >= end:
    return

  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  less_than_pointer = start

  for i in range(start, end):
    if list[i] < pivot_element:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1

  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quick_sort(list, start, less_than_pointer - 1)
  quick_sort(list, less_than_pointer + 1, end)



"""Sort given items in place by partitioning items in range `[low...high]`
around a pivot item and recursively sorting each remaining sublist range.
TODO: Best case running time: ??? Why and under what conditions?
TODO: Worst case running time: ??? Why and under what conditions?
TODO: Memory usage: ??? Why and under what conditions?
TODO: Check if high and low range bounds have default values (not given)
TODO: Check if list or range is so small it's already sorted (base case)
TODO: Partition items in-place around a pivot and get index of pivot
TODO: Sort each sublist range by recursively calling quick sort"""
