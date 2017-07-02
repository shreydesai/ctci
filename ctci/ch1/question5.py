def one_away(s1, s2):
    if len(s1) == len(s2):
        return one_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_insert(s2, s1)
    return False


def one_replace(s1, s2):
    edited = False
    for i, j in zip(s1, s2):
        if i != j:
            if edited:
                return False
            edited = True
    return True


def one_insert(s1, s2):
    edits, i, j = 0, 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i, j = i + 1, j + 1
        else:
            edits += 1
            if edits > 1:
                return False
            j += 1
    return edits <= 1
