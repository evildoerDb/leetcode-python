def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    first = 0
    second = 0

    res = []

    while (first < m) and (second < n):
        if nums1[first] < nums2[second]:
            res.append(nums1[first])
            first += 1
        else:
            res.append(nums2[second])
            second += 1

    if first < m:
        while first < m:
            res.append(nums1[first])
            first += 1

    if second < n:
        while second < n:
            res.append(nums2[second])
            second += 1

    return res


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    res = merge(nums1, 3, nums2, 3)

    # for num in res:
    #     print(num)
    print(res)
