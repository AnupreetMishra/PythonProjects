string = input("Enter the string: ")
strlist = list(string)
sortedString = ''.join(sorted(strlist, reverse = True))
print("Sorted string in descending order: ", sortedString)
