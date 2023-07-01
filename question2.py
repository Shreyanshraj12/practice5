def num_complete_rows(n):
    k = 1
    while (k * (k + 1)) / 2 <= n:
        k += 1
    return k - 1
print(num_complete_rows(5)) 
print(num_complete_rows(10))  
print(num_complete_rows(15))  
