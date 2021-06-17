class Solution(object):

    def move_zero_end_of_list(self, numbers):

        last_zero_index = len(numbers)

        for idx in range(len(numbers)):
            curr_num = numbers[idx]

            if curr_num == 0:
                last_zero_index = min(last_zero_index, idx)
            elif curr_num != 0 and last_zero_index < len(numbers):
                numbers[last_zero_index], numbers[idx] = curr_num, 0
                last_zero_index += 1

    # Another Solution
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1



if __name__ == '__main__':
    lst = [0, 1, 0, 3, 12]
    sol = Solution()
    sol.move_zero_end_of_list(lst)
    print(lst)

    lst = [1,0,1]
    sol.move_zero_end_of_list(lst)
    print(lst)

    lst = [1,0,0,0,1]
    sol.move_zero_end_of_list(lst)
    print(lst)