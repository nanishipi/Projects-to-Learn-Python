def missing_character(string, n):
    if len(string):
        string = string[:n] + string[n+1:]
        print(string)
        return string
    else:
        print('Empty String')
print(missing_character('banana', 3))