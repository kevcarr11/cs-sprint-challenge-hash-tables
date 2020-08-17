def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    integers = dict()
    result = []

    for num in a:
         # if the num has a corresponding number in the dict
        if integers.get(abs(num)):
            # check if they add to 0
            if (integers.get(abs(num)) + num) == 0:
                result.append(abs(num))

        else:
             # if no value is found, pass num as new key along with it's value
            integers[abs(num)] = num
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
