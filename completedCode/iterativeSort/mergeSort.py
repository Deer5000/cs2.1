def merge_sort(items):
    if len(items) <= 1:
        return items
    
    mid_idx = len(items) // 2
    left_split = items[:mid_idx]
    right_split = items[mid_idx:]

    left_sort = merge_sort(left_split)
    right_sort = merge_sort(right_split)

    return merge(left_sort, right_sort)


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


