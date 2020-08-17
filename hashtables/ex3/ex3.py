def intersection(arrays):
    """
    for i in arrays = each index in arrays []. 
    arrays = [           
        index 0 [1, 2, 3, 4, 5],
        index 1 [12, 7, 2, 9, 1],
        index 2 [99, 2, 7, 1,]
        ]
    for j in i = need to go deeper to find each i of index
        index 0 [1, 2, 3, 4, 5]
            i = [0, 1, 2, 3, 4]
    """
    cache = dict()
    result = []

    for i in arrays:
        for j in i:
            if j in cache:
                cache[j] += 1
            else:
                cache[j] = 1
    
    for new_list in cache:
        if cache[new_list] == len(arrays):
            result.append(new_list)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
