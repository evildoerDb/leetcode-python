'''

You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.
 Each character in S is a type of stone you have.
 You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct,
and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

S中的每个字母代表一种类型 J代表你拥有的类型
实际就是计算出你拥有的类型

    771
'''


def numJewelsInStones(self, J, S):
    """
    :param self:
    :type J: str
    :type S: str
    :rtype: int
    """
    count = 0
    for index in range(len(S)):
        if S[index] in J:
            count += 1
    return count


def numJewelsInStones2(self, J, S):
    """
    :param self:
    :type J: str
    :type S: str
    :rtype: int
    """
    count = 0
    for char in J:
        count += S.count(char)
    return count


if __name__ == '__main__':
    print(numJewelsInStones("", "aA", "aAAbbbb"))
