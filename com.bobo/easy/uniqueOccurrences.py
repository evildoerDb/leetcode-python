from typing import List

'''
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
'''


def uniqueOccurrences(arr: List[int]) -> bool:
    res = {}
    for num in arr:
        if num not in res.keys():
            res[num] = 1
        else:
            result = res[num]
            result += 1
            res[num] = result

    values = res.values()

    return len(values) == len(set(values))


if __name__ == '__main__':
    arr = [1, 2]

    print(uniqueOccurrences(arr))


