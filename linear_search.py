def sequential_search(data, key):
    for index in range(len(data)):
        if key == data[index]:
            return index, data[index]

    return -1

data = [-5, 5, 10, 15, 20, 50, 100, 150, 200, 300]
print(sequential_search(data, 100))
