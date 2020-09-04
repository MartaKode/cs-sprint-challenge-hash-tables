def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    weight_index = {}

    index = 0

    # store the indexes as values and weights as keys
    for num in weights:
        # if we have dupes, needs to signify it
        if num in weight_index:
            weight_index[num, 'dupe'] = index
        else:   
            weight_index[num] = index
        index += 1

    # return weight_index

    # check each weight in hash table
    for key in weight_index:
        # if we have dupes, dupe is the bigger index
        if (limit - key) in weights and (limit - key) == key:
            big_index = weight_index[key, 'dupe']
            small_index = weight_index[key]
            return [big_index, small_index]

        # if the key has a corresponding fill in weights , save them
        if (limit - key) in weights:
            small_index = weight_index[key]
            big_index = weight_index[limit - key]
            return [big_index, small_index]



    return None


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)
