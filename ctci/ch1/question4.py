def palindrome_permutation(string):
    char_map = {}
    chars = [c.lower() for c in string]

    for char in chars:
        if char in char_map:
            char_map[char] -= 1
        else:
            char_map[char] = 1

    above_zero = 0

    for k in char_map.keys():
        if char_map[k] > 0:
            above_zero += 1

    if len(chars) % 2 == 0:
        return above_zero == 2
    else:
        return above_zero == 1
