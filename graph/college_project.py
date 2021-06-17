d3 = {'A': ['A', 'B', 'C', 'D'],
      'B': ['A', 'B', 'C', 'D'],
      'C': ['A', 'B', 'C', 'D'],
      'D': ['A', 'B', 'C', 'D']}

out_lst = []


def recursion_for_combinations(key, bld_comb):
    if len(bld_comb) == 7:
        out_lst.append(bld_comb)
        print(bld_comb)
        bld_comb = 'A'
        # return bld_comb

    for bld in d3[key]:
        if bld not in bld_comb and bld != key:
            bld_comb += ':' + bld
            recursion_for_combinations(bld, bld_comb)


recursion_for_combinations('A', 'A')