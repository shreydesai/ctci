def string_compression(string):
    cstring = []

    curr = string[0]
    count = 0

    for char in string:
        if char == curr:
            count += 1
        else:
            cstring.append('{}{}'.format(curr, count))
            curr = char
            count = 1

    cstring.append('{}{}'.format(curr, count))
    cstring = ''.join(cstring)

    if len(cstring) < len(string):
        return cstring
    else:
        return string
