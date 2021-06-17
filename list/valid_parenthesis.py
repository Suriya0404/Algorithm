class Solution(object):

    def check_valid_parenthesis(self, sent):

        if not sent or sent is None or len(sent) < 2:
            return False

        close_pat = {'}': '{',
                     ')': '(',
                     ']': '[',
                     '>': '<'}

        open_pat = {pat[1]: pat[0] for pat in close_pat}

        pat_log = []

        for par in sent:
            if par in open_pat:
                pat_log.append(par)
            elif par in close_pat:
                if len(pat_log) == 0:
                    return False
                else:
                    last_par = pat_log.pop()
                    if last_par != close_pat[par]:
                        return False

        return True if len(pat_log) == 0 else False


if __name__ == '__main__':
    sol = Solution()

    pat = '()({})<<>>'
    print(sol.check_valid_parenthesis(pat))

    pat = '()({})<<>>>'
    print(sol.check_valid_parenthesis(pat))

    pat = '>()({})<<>>>'
    print(sol.check_valid_parenthesis(pat))

    pat = '>()({})<<>>>'
    print(sol.check_valid_parenthesis(pat))
