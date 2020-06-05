# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    filenames_dict = {}
    result = []
    for filename in files:
        words = filename.split("/")
        # the last word is a file name
        if words[-1] not in filenames_dict:
            filenames_dict[words[-1]] = [filename]
        else:
            filenames_dict[words[-1]].append(filename)

    for query in queries:
        if query in filenames_dict:
            for f in filenames_dict[query]:
                result.append(f)

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
