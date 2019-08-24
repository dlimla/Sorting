# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    left, right = 0, 0
    middle = 0

    # while left < len(arrA) and right < len(arrB):
    #     if arrA[left] < arrB[right]:
    #         merged_arr.append(arrA[left])
    #         left += 1
    #     else:
    #         merged_arr.append(arrB[right])
    #         right += 1

    while middle < len(merged_arr):
        if left == len(arrA):
            merged_arr[middle] = arrB[right]
            right += 1
        elif right == len(arrB):
            merged_arr[middle] = arrA[left]
            left += 1
        elif arrA[left] < arrB[right]:
            merged_arr[middle] = arrA[left]
            left += 1
        else:
            merged_arr[middle] = arrB[right]
            right += 1
        middle += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0:
        return []

    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)//2
        left = merge_sort(arr[0:middle])
        right = merge_sort(arr[middle:len(arr)])
        return merge(left, right)
    # return merge(merge_sort(arr[:middle]),merge_sort(arr[middle:]))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
