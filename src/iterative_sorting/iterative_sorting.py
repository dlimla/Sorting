# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for j in range(i+1,len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j



        # TO-DO: swap
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



    return arr

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        first_index = i
        next_index = i+1
        # if(next_index < first_index):
        if(arr[i] > next_index):
            arr[first_index], arr[next_index] = arr[next_index], arr[first_index]
    return arr

arr1 = [3,4]

print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr