
def sequential_search(num_list, number):
    for ind in range(len(num_list)):
        if num_list[ind] == number:
            return True
    return False

for shape in ['spear', 'diamond', 'club', 'hearts']



if __name__ == '__main__':
    num_list1 = [1, 2, 3, 4, 5]
    print(sequential_search(num_list1, 4))
    print(sequential_search(num_list1, 10))
