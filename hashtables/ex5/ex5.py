# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    file_query = {}

    # split_files = []

    # maybe split files into array of arrays?
    for file_name in files:
        # split_files.append(file_name.split("/"))
        # paths as keys and everything inside the path as values
        # file_query[tuple(file_name.split("/"))] = file_name

        file_query[file_name] = file_name.rsplit("/", 1)[-1]
        # file_query[file_name.rsplit("/", 1)[-1]] = file_name

    # inverted = {value: key for key,value in file_query.items()}

    for key in file_query:
        if file_query[key] in queries:
                result += [key]

    # for query in queries:
    #     if file_query.get(query):
    #         result += [file_query[query]]

    

    # return file_query
    # return split_files

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
