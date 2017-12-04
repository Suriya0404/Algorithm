"""
Big O Notation
time complexity
O(1) = Constant
O(n) = linear
O(n2) = quadratic

Space complexity


"""



import timeit

def sum1(number):

    a = 0
    for num in range(number):
        a += num

    return a

def sum2(n):
    return n * (n + 1)/2

if __name__ == '__main__':
    timeit.timeit(sum1(100))
    # timeit.timeit(sum2(100), number=10000)

