def is_unique(string):
    letters = {}

    for char in string:
        if char in letters:
            return False
        else:
            letters[char] = 1

    return True


def is_unique_2(string):
    letters = list(string)

    for i in range(len(letters)):
        for j in range(len(letters)):
            if i != j and letters[i] == letters[j]:
                return False

    return True
