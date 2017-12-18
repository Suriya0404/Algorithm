from itertools import groupby


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for outer in range(len(nums)):
            print('***************************')
            pntLeft = outer + 1
            pntRght = len(nums) - 1

            while pntRght > pntLeft:
                print('outer : ' + str(nums[outer]))
                print('Left : ' + str(nums[pntLeft]))
                print('Right : ' + str(nums[pntRght]))
                print('Pointer Right :' + str(pntRght))
                print('Pointer Left : ' + str(pntLeft))

                if nums[outer] + nums[pntRght] + nums[pntLeft] == 0:
                    result.append(sorted([nums[outer], nums[pntRght], nums[pntLeft]]))
                    pntLeft += 1
                elif nums[outer] + nums[pntRght] + nums[pntLeft] < 0:
                    pntLeft += 1
                elif nums[outer] + nums[pntRght] + nums[pntLeft] > 0:
                    pntRght -= 1

        # return list(l for l, _ in groupby(result))
        return list(result[curr] for curr in range(len(result)) if curr == 0 or result[curr] != result[curr - 1])