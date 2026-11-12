string = input("Enter a word: ")
string2 = ('')
for i in string:
    string2 = i + string2


print("Original text: ", string)
print("Reversed string: ", string2)