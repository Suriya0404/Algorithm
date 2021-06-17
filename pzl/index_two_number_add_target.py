class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for idx, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], idx]
            else:
                seen[num] = idx

        return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]

    s = Solution()

    print(s.twoSum(nums, 9))






