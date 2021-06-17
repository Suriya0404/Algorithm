class Solution(object):

    def is_palindrome(self, istr):

        left_ptr = 0
        right_ptr = len(istr) - 1

        while left_ptr < right_ptr:
            if not istr[left_ptr].isalnum():
                left_ptr += 1
            elif not istr[right_ptr].isalnum():
                right_ptr -= 1
            elif istr[left_ptr].lower() == istr[right_ptr].lower():
                left_ptr += 1
                right_ptr -= 1
            elif istr[left_ptr].lower() != istr[right_ptr].lower():
                return False

        return True

    def palindrome_check(self, list_str):
        return [self.is_palindrome(in_str) for in_str in list_str]


if __name__ == '__main__':
    input1 = ["A man, a plan, a canal - Panama",
              "Able was I ere I was Elba",
              "Madam, I'm Adam",
              "hannah",
              "test"]

    sol = Solution()
    print(sol.palindrome_check(input1))



