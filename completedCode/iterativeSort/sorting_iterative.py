list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 1, 6, 9, 12, 3]
list3 = [1, 2, 3, 4, 5, 6, 7]
list4 = [4, 5, 1, 6, 9, 12, 3, 123, 24, 72, 1, 0]
list5 = [1, 2, 3, 4, 5, 6, 7]
list6 = [4, 5, 1, 6, 9, 12, 3]
list7 = [1,2,3,4,5,6,7]
list8 = [2,6,7,2,9,0,6,34]





def is_sorted(items):
    error = 0
    i = 1
    while i < len(items):
        if items[i] < items[i-1]:
            error = 1
        i += 1

    if error >= 1:
        return False
    else:
        return True

print(is_sorted(list7))
print(is_sorted(list8))


#     """Return a boolean indicating whether given items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    for i in range(len(items)):
        for idx in (range(len(items) - i - 1)):
            if items[idx] > items[idx + 1]:
                items[idx], items[idx + 1] = items[idx + 1], items[idx]
    print(items)

bubble_sort(list1)
bubble_sort(list2)

    # """Sort given items by swapping adjacent items that are out of order, and
    # repeating until all items are in sorted order.
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?"""
    # # TODO: Repeat until all items are in sorted order
    # # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    for i in range(len(items)):
        min_idx = i
        for idx in range(i+1, len(items)):
            if items[min_idx] > items[idx]:
                min_idx = idx
        items[i], items[min_idx] = items[min_idx], items[i]
    return items

print(selection_sort(list3))
print(selection_sort(list4))
        
#     """Sort given items by finding minimum item, swapping it with first
#     unsorted item, and repeating until all items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Find minimum item in unsorted items
#     # TODO: Swap it with first unsorted item


def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        n = i - 1
        while n >= 0 and key < items[n]:
            items[n + 1] = items[n]
            n -= 1
        items[n + 1] = key
    print(items)
insertion_sort(list5)
insertion_sort(list6)



#     """Sort given items by taking first unsorted item, inserting it in sorted
#     order in front of items, and repeating until all items are in order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Take first unsorted item
#     # TODO: Insert it in sorted order in front of items
