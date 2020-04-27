from typing import List

'''
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
'''
def sort_array_by_parity(A: List[int]) -> List[int]:
    n = len(A)
    left = 0
    right = n - 1

    while left < right:
        while A[left] % 2 == 0 and left < right:
            left += 1
        while A[right] % 2 == 1 and right > left:
            right -= 1
        temp = A[left]
        A[left] = A[right]
        A[right] = temp
        left += 1
        right -= 1
    return A


if __name__ == '__main__':
    A = [3, 1, 2, 4]
    s = sort_array_by_parity(A)
    print(s)
