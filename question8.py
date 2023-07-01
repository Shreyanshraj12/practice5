def find_original(changed):
    original = []

    for num in changed:
        if num / 2 in original:
            original.remove(num / 2)
        else:
            original.append(num)

    if len(original) == 0:
        return original
    else:
        return []

changed = [1, 3, 4, 2, 6, 8]
print(find_original(changed))
