def report(file, *details):
    for i in details:
        if i:
            print(i, end=" ")
    if file != None: print(file)
