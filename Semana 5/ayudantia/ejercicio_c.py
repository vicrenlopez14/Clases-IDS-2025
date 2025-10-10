if __name__ == '__main__':
    # Receive num
    num = int(input())
    iterations=0

    # Until 1
    while num > 1:
        if (num % 2 == 0):
            num = num / 2
        else:
            num = (num * 3) + 1
        # Increase the iterations
        iterations +=1

    # Print it
    print(iterations)