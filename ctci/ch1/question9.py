def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        return s1 in (s2 + s2)
