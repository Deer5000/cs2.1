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
TODO: Best case running time: O(n log n)✅
TODO: Worst case running time: O(n2)✅
TODO: Memory usage: O(log n)✅"""
