class Solution(object):

    def merge_intervals(self, intervals):

        if not intervals:
            return None

        merged_intervals = []

        intervals.sort(key=lambda x: x[0])
        curr_sess_start = intervals[0][0]
        curr_sess_end = intervals[0][1]
        merged_intervals.append([curr_sess_start, curr_sess_end])
        idx = 1

        while idx < len(intervals):
            next_sess_start = intervals[idx][0]
            next_sess_end = intervals[idx][1]

            if next_sess_start <= curr_sess_end < next_sess_end:
                merged_intervals[-1][1] = next_sess_end
                curr_sess_end = next_sess_end
                idx += 1
            elif next_sess_start > curr_sess_end:
                merged_intervals.append([next_sess_start, next_sess_end])
                curr_sess_start = next_sess_start
                curr_sess_end = next_sess_end
                idx += 1
            else:
                idx += 1

        return sum([inter[1] - inter[0] for inter in merged_intervals])


if __name__ == '__main__':
    lst = [[1, 3], [2, 6], [8, 10], [15, 18]]

    sol = Solution()
    print(sol.merge_intervals(lst))



