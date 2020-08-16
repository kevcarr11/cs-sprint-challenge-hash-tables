def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    values = dict()

    if length <= 1:
       return None

    # Traverse weights only once. For each weight w in weights compute its complement limit - w and checkwhether that
    # complement is hashed so far. If found the complement in the map, return a pair that consists of
    # w’s and limit - w’s indices. if not, hash w while using the weight as the hash key and its array index as the hash
    # value. Even if the same weight is found more than once it doesn’t matter because at the time of the lookup we only
    # need one item with that weight

    for i in range(length):
        weight = weights[i]
        if weight in values:
            value = values[weight]
            return [i, value]
        diff = limit - weight
        values[diff] = i

    return None
