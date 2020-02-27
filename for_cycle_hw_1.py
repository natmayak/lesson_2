#v.1
print(*range(0, 10))

#v.2
for number in range(10):
    print(number, end = " ")
print()

#v.3
for number in range(10):
    #number = number + 1
    print(number)
#v.4
lst = []
for elem in range(10):
    lst.append(elem)
print(lst)

print("Give me some text ")
text = input()
for letter in text.split():
    print(f'{letter.upper()}')

print("Give me some text")
text = input()
for letter in text:
    print(letter)

#for number in range(3):
	#print(f"Привет мир {number}!")

#for letter in "python":
    #print(letter.upper())

#example_string = "Я учу язык python"

#for word in example_string.split():
    #print(f'Длина слова "{word}": {len(word)}')
