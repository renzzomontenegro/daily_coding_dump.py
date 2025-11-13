from collections import deque

def shift_array(arr, n):
    if n >= 1:
        arr = deque(arr)
        arr.rotate(n)
        return list(arr)
    if n < 0:
        arr = deque(arr)
        arr.rotate(n)
        return list(arr)
    if n == 0:
        return arr
    
    return list(arr)

x = [1, 2, 3]

print(f"\n{x}")

y = shift_array(x, -1)

print(f"\n{y}")