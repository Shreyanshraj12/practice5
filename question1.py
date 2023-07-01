def convert_to_2d_array(original, m, n):
    length = len(original)
    if length != m * n:
        return []
    
    result = [[0] * n for _ in range(m)]
    for i in range(length):
        row = i // n
        col = i % n
        result[row][col] = original[i]
    
    return result
original = [1, 2, 3, 4, 5, 6]
m = 2
n = 3

result = convert_to_2d_array(original, m, n)
print(result)
