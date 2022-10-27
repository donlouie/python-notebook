def count_positives_sum_negatives(arr):
    pos_count = 0
    neg_sum = 0

    if arr == [] or arr == None:
        return []

    for i in range(len(arr)):
        if(arr[i] > 0):
            pos_count += 1
        else:
            neg_sum += arr[i]
    return ([pos_count, neg_sum])


print(count_positives_sum_negatives(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# return [10, -65]


# Other solution
# Solution 1


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        if x < 0:
            neg += x
    return [pos, neg]

# Solution 2


def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []
