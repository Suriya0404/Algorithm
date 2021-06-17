class Solution(object):

    def identify_max_frequency(self, numbers):
        max_frequency = 0
        number_counter = {}

        for num in numbers:
            number_counter[num] = number_counter.get(num, 0) + 1
            max_frequency = max(max_frequency, number_counter[num])

        return max_frequency, number_counter

    def make_same_frequency(self, numbers):
        max_frequency, counter = self.identify_max_frequency(numbers)

        for num, val in counter.items():
            for _ in range(max_frequency - val):
                numbers.append(num)


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3, 3, 3, 3]
    sol.make_same_frequency(nums)
    print(nums)

    nums = [1, 1, 2, 2, 3, 3]
    sol.make_same_frequency(nums)
    print(nums)
