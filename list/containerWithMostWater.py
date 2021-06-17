# Below answer is incorrect.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int


        """

        # loop for every element in list
        # from that element iterate forward and find the area.
        # if the area found is greater than max area found replace it.
        # return max area
        max_area = 0

        for idx, val in enumerate(height):
            for idxn in range(idx + 1, len(height)):
                min_height = min(height[idx], height[idxn])
                area = min_height * (idxn - idx)
                max_area = max(max_area, area)

        return max_area


    def max_area2(self, height):
        # Set two pointers left and right
        # if left > right decrement right
        # if right > left decrement left
        # if right = left decrement left
        # do this until left less than right
        # calculate area for each step
        # return the max area.

        lpoint = 0
        rpoint = len(height) - 1
        max_area = 0

        while lpoint < rpoint:
            lheight = height[lpoint]
            rheight = height[rpoint]
            min_height = min(lheight, rheight)
            area = min_height * (rpoint - lpoint)
            max_area = max(max_area, area)

            if height[lpoint] >= height[rpoint]:
                rpoint -= 1
            else:
                lpoint += 1

        return max_area


if __name__ == '__main__':
    inList = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # Output: 49
    sol = Solution()
    print(sol.maxArea(inList))

    print(sol.max_area2(inList))

