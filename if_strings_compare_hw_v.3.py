def strings_compare(string1, string2):
    if type(string1) != str or type(string2) != str:
        return 0
    elif string1 == string2:
        return 1
    elif string1 != string2 and string2 == "learn":
        return 3
    elif len(string1) > len(string2):
        return 2

print(strings_compare("kknnnk", "learn"))
