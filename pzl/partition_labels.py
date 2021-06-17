class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        max_let = {let: idx for idx, let in enumerate(S)}

        output = []
        max_idx = prev_idx = 0
        for idx, let in enumerate(S):
            max_idx = max(max_idx, max_let[let])

            if idx == max_idx:
                output.append(idx + 1 - prev_idx)
                prev_idx = idx + 1

        return output

if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"

    sol = Solution()

    out = sol.partitionLabels(S)

    print('out: ' + str(out))
