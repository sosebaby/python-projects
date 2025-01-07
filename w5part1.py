data = "Python rules!"

#Obtain list of the words in the string
print('List of words in the string: ', data.split())
#Convert string to lowercase
print('String in lower case: ', data.lower())

#Locate the position of string “rules”
print("Position of 'rules': ", data.find("rules"))
#Replace the exclamation point with a question mark
print("Replacing exclamation mark with question mark: ", data.replace("!", "?"))
#Print only the substring ‘thon’ of the string
print("Printing only 'thon': ", data[2:6])
#prints the string in reverse.
print("Printing string in reverse: ", data[::-1])
