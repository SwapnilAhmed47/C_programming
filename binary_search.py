# User define 
def binary_search(data, size, key):
    left = 0
    right = size -1 
    while left <= right:
        mid_index = (left + right)//2
        mid_val = data[mid_index]
        if key == mid_val:
            return mid_index
        elif key > mid_val:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1

data = [-5, 5, 10, 15, 20, 50, 100, 150, 200, 300]
print(binary_search(data, len(data), 5))
