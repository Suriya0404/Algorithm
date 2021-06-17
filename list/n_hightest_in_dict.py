
class Solution(object):

    def find_nth_key(self, in_dict, top_n_position):
        if not in_dict or top_n_position < 1:
            return None

        sort_tuple = sorted(in_dict.items(), key=lambda x: x[1], reverse=True)
        return sort_tuple[top_n_position - 1][0]

