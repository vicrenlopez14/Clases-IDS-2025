if __name__ == '__main__':
    # Degrees
    degrees = ("LEN", "IDN", "LCJ", "ISND")

    # Get affinities and parse
    affinities = [int(input()) for _ in range(4)]

    # Order them
    max_index = affinities.index(max(affinities))

    # Print biggest one
    print(degrees[max_index])
