def word_frequency(sentence):
    words = sentence.split()

    # Initialize an empty dictionary to store the word frequencies
    frequency_dict = {}

    # Iterate through the list of words
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            # Otherwise, add the word to the dictionary with a count of 1
            frequency_dict[word] = 1

    return frequency_dict

# Input: Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Call the word_frequency function and print the resulting dictionary
print(word_frequency(sentence))
