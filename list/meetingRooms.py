class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        starts, ends = [], []
        for i in intervals:
            starts.append(i[0])
            ends.append(i[1])

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1

        return min_rooms

    def myMinMeetingRooms(self, intervals):
        """
         :type intervals: List[List[int]]
         :rtype: int
        """
        start_time = []
        end_time = []

        for inter in intervals:
            start_time.append(inter[0])
            end_time.append(inter[1])

        start_time.sort()
        end_time.sort()

        eidx = 0
        sidx = 0
        meeting_room = 0
        min_room = 0

        while sidx < len(intervals):
            st = start_time[sidx]
            et = end_time[eidx]

            if st < et:
                meeting_room += 1
                min_room = max(min_room, meeting_room)
                sidx += 1
            else:
                eidx += 1
                meeting_room -= 1

        return min_room


if __name__ == '__main__':
    # inp = [[0, 30], [5, 10], [15, 20]]
    # Output: 2

    # Input: [[7, 10], [2, 4]]
    # Output: 1
    inp = [[1,5],[8,9],[8,9]]

    sol = Solution()

    # print(sol.minMeetingRooms(inp))
    print(sol.myMinMeetingRooms(inp))
