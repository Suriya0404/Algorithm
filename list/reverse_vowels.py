class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lpoint = 0
        rpoint = len(s) - 1
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        out_str = list(s)

        while lpoint < rpoint:
            lchar = s[lpoint]
            rchar = s[rpoint]

            if lchar not in vowel:
                lpoint += 1

            if rchar not in vowel:
                rpoint -= 1

            if lchar in vowel and rchar in vowel:
                out_str[lpoint] = rchar
                out_str[rpoint] = lchar
                lpoint += 1
                rpoint -= 1

        return ''.join(out_str)


