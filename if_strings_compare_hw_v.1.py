def strings_compare(string1, string2):
    if not string1.isdigit():
        print("true")
    else:
        print("0")
    if not string2.isdigit():
        print("true")
    else:
        print("0")

print("input text1")
string1 = (input())
print("input text2")
string2 = (input())
strings_compare(string1, string2)