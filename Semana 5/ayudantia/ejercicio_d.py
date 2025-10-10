if __name__ == '__main__':
    # Get size
    size = len(input())

    # Get elements
    elem = [int(e) for e in input().split()]

    # Sort them and print the min
    minIndex = elem.index(min(elem))

    print(minIndex + 1)