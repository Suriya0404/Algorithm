"""
Champagne Tower:

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th
row. Each glass holds one cup (250ml) of champagne.

Then, some champagne is poured in the first glass at the top.  When the top most glass is full, any excess liquid poured
will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess
champagne will fall equally to the left and right of those glasses, and so on.
(A glass at the bottom row has it's excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured,
the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full
- there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass
half full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is
(both i and j are 0 indexed.)

Example 1:
Input: poured = 1, query_glass = 1, query_row = 1
Output: 0.0
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)).
There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_glass = 1, query_row = 1
Output: 0.5
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)).
There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess
liquid equally, and each will get half cup of champange.


Note:

poured will be in the range of [0, 10 ^ 9].
query_glass and query_row will be in the range of [0, 99].

"""
def champagneTower(poured, query_row, query_glass):
    """
    :type poured: int
    :type query_row: int
    :type query_glass: int
    :rtype: float
    """
    glass = {}

    if poured == 0:
        return 0.0

    for _ in range(poured):
        pour = 1
        layer = 0
        while layer < 99 and pour > 0:
            if layer == 0:
                split = 1
            else:
                split = 2 * layer

            for col in range(layer + 1):
                if pour > 0:
                    if (col == 0) or (col == layer):    # glasss on the edge will get only from one glass above
                        if str(layer) + ":" + str(col) not in glass:
                            glass[str(layer) + ":" + str(col)] = 1 / split
                            pour -= 1 / split
                        elif glass[str(layer) + ":" + str(col)] < 1:
                            glass[str(layer) + ":" + str(col)] += 1 / split
                            pour -= 1 / split
                        elif glass[str(layer) + ":" + str(col)] == 1:
                            continue
                    else:                               # glasses in between will get from two glasses above.
                        if str(layer) + ":" + str(col) not in glass:
                            glass[str(layer) + ":" + str(col)] = 2 / split
                            pour -= 2 / split
                        elif glass[str(layer) + ":" + str(col)] < 1:
                            glass[str(layer) + ":" + str(col)] += 2 / split
                            pour -= 2 / split
                        elif glass[str(layer) + ":" + str(col)] == 1:
                            continue

            layer += 1

    if str(query_row) + ":" + str(query_glass) in glass:
        return glass[str(query_row) + ":" + str(query_glass)]
    else:
        return 0.0

if __name__ == '__main__':

    glass_pour = 6
    row = 3
    column = 0

    output = champagneTower(glass_pour, row, column)
    print('After pouring {0} glasses of champagne the glass on {1} row and {2} column will have {3} glass of champange'.
          format(glass_pour, row, column, output))
