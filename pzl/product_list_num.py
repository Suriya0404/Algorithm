"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        for idx in range(len(nums)):
            copy_lst = nums[:]
            del copy_lst[idx]
            output.append(reduce(lambda x, y: x * y, copy_lst))

        return output


if __name__ == '__main__':
    lst = [1,2,3,4]
    sol = Solution()
    out = sol.productExceptSelf([1,2,3,4])
    print(out)




