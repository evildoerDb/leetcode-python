class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1
        index = m + n - 1

        while (first >= 0) and (second >= 0):
            if nums1[first] < nums2[second]:
                nums1[index] = nums2[second]
                second -= 1

            else:
                nums1[index] = nums1[first]
                first -= 1
            index -= 1

        if first >= 0:
            while first >= 0:
                nums1[index] = nums1[first]
                first -= 1
                index -= 1

        if second >= 0:
            while second >= 0:
                nums1[index] = nums2[second]
                second -= 1
                index -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    s = Solution()
    s.merge(nums1, 3, nums2, 3)

    # for num in res:
    #     print(num)
    print(nums1)
