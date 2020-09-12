def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
   # Establishing dictionary for values
    the_cache = {}
    sm_index = 0
    lrg_index = 0
    # Looping through list and put the values in the dictionary
    for i in range(len(weights)):

        if weights[i] not in the_cache:
            the_cache[weights[i]] = i
            if limit - weights[i] == weights[i]:
                continue
        if limit - weights[i] in the_cache:
            # finding out what is the smaller of the two values min = a if a < b else b
            if i > the_cache[limit - weights[i]]:
                sm_index = the_cache[limit - weights[i]]
                lrg_index = i
            else:
                sm_index = i
                lrg_index = the_cache[limit - weights[i]]
            return (lrg_index, sm_index)

    return None
