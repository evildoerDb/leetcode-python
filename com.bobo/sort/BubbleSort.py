def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j)


if __name__ == '__main__':
    arr = [24, 23, 1, 34, 43, 4, 6]
    bubbleSort(arr)
    for i in range(len(arr)):
        print(arr[i], end=" ")
