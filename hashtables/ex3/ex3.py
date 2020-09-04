def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    number_of_arrays = len(arrays)

    dupes = {}

    # array of arrays: go over each array
    for array in arrays:
        # go over values of each nested array
        for num in array:
            # if the value is not in dupes, set it to 1
            if num not in dupes:
                dupes[num] = 1
            # otherwise, already exists in dupes, bump the counter
            else:
                dupes[num] += 1

    for key in dupes:
        # if the number appeared as many times as long is the main array, it must be present in ALL nested arrays
        if dupes[key] == number_of_arrays:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
