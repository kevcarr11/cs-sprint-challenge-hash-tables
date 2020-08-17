
def finder(files, queries):
  
    result = []
    # stored file names
    f_table = dict()
    # stored queries
    q_table = dict()

    # loop through files and store file names as keys in dict
    for f in files:
        f_table[f] = None

    # loop through queries and store each query as keys in dict 
    for q in queries:
        q_table[q] = None

    for key in f_table:
        # remove / and split filename from path
        filename = key.split('/')[-1]
        # if filename exists in query table then add to result 
        if filename in q_table:
            result.append(key)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
