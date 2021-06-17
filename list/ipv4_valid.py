class Solution(object):

    def check_ipv4_validity(self, ipv4_address):
        if not ipv4_address:
            return False
        elif len(ipv4_address) < 7 or len(ipv4_address) > 15:
            return False
        elif len(ipv4_address.split('.')) != 4:
            return False

        for sub in ipv4_address.split('.'):
            try:
                if int(sub) < 0 or int(sub) > 255:
                    return False
            except ValueError as ex:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()

    print(sol.check_ipv4_validity("192.192.192.0"))
    print(sol.check_ipv4_validity("255.255.255.255"))
    print(sol.check_ipv4_validity("0.0.0.0"))
    print(sol.check_ipv4_validity("0.0.0.0a"))
    print(sol.check_ipv4_validity("0.0.0.257"))


