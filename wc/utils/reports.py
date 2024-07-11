def report(file, *details):
    for i in details:
        if i != False:
            print(i, end=" ")
    print(file)
