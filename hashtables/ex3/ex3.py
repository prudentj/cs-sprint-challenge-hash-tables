def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Get the number of lists
    num_lists = len(arrays)
    result = []
    # One dic will hold the values that haven't been confirmed
    # the value really doesn't matter here only the key does
    unconfirmed_dict = {}
    # This dict holds values that are confirmed to exist in the previous dict
    comfirmed_dict = {}
    # at the end of each round we will make the unconfirmed dict equal a confirmed one
    # and empty the confrimed one
    for index in range(num_lists):
        # nothing exists in unconfirmed so I add all the numbers to the dictionary and move to next list
        current_list = arrays[index]
        if index == 0:
            for num in current_list:
                unconfirmed_dict[num] = 1
        else:
            for num in current_list:
                if num in unconfirmed_dict:
                    comfirmed_dict[num] = 1
            unconfirmed_dict = comfirmed_dict
            comfirmed_dict = {}
    # For the last round comfirmed dict is empty and we now need to put the values in a list
    for key in unconfirmed_dict:
        result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
