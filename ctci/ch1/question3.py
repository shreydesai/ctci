def urlify(string):
    string = string.strip()
    words = string.split(' ')
    return '%20'.join(words)
