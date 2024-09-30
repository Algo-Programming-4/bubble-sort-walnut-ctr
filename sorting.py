def bubble(ary):
    """sorts an array with bubble sort"""
    sorted = False
    times = len(ary)
    while sorted == False:
        sorted = True
        times -= 1
        for i in range(times):
            if ary[i] > ary[i+1]:
                sorted = False
                checking = 0
                swap = ary[i+1]
                ary[i+1] = ary[i - checking]
                ary[i] = swap
    return ary


def main():
    test_ary = [6,3,2,5,4]
    print(bubble(test_ary))


if __name__ == "__main__":
    main()
            