

class Solution(object):

    def is_prime(self, number):
        for num in range(2, number - 1):
            if number % num == 0:
                return False

        return True

    def optimized_is_prime(self, number):
        if number < 2:
            return False

        if number in (2, 3, 5, 7):
            return True

        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            return False

        for num in range(5, number // 2):
            if number % num == 0:
                return False

        return True

    def find_prime_number(self, lst):
        lst_prime = []
        for number in lst:
            if self.optimized_is_prime(number):
                lst_prime.append(number)
        return lst_prime


if __name__ == '__main__':
    sol = Solution()
    print(sol.find_prime_number(range(100)))
