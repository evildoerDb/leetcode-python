from typing import List

'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
'''


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    # res = []
    # for i in nums1:
    #     for j in nums2:
    #         if i == j:
    #             res.append(i)
    #             break
    #
    # res = set(res)
    # return res
    temp = set(nums1)
    res = []
    for num in nums2:
        if num in temp:
            res.append(num)

    return set(res)


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    res = intersection(nums1, nums2)
    print(res)
