class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        result = False

        if (x2 > x3 and y2 > y3) and (x1 < x4) and (y1 < y4):
            result = True

        return result

    def futher_optimized(self, rec1, rec2):
        return (rec1[2] > rec2[0] and rec1[3] > rec2[1]) and (rec1[0] < rec2[2]) and (rec1[1] < rec2[3])
