def trim(s):
    i = 0
    j = len(s) - 1
    while i < j and (s[i] == ' ' or s[j] == ' '):
        if s[i] == ' ':
            i += 1
        if s[j] == ' ':
            j -= 1
    return s[i:j + 1]

print(trim('     hello '))