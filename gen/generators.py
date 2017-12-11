

def fsum(start, end, increment=1):
    curr = start
    while curr <= end:
        yield curr
        curr += increment

if __name__ == '__main__':

    print(fsum(1, 10, 1))

    for value in fsum(1,10,1):
        print(value)