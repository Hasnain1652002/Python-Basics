# function of counting letter occurrences in a given list of words
def count_letter_frequencies(word_list):
    frequency_map = {}  # ddictionary to store letter counts

    # combine all words into a single string
    combined_string = ""
    for word in word_list:
        combined_string += word  # appending words together

    # counting occurrences of each letter
    for character in combined_string:
        if character in frequency_map:
            frequency_map[character] += 1
        else:
            frequency_map[character] = 1
    
    return frequency_map

# function of determining the most frequently occurring letter
def find_most_common_letters(frequency_map):
    highest_frequency = 0
    common_letters = set()

    # finding the highest frequency
    for frequency in frequency_map.values():
        if frequency > highest_frequency:
            highest_frequency = frequency

    # identifying the letters with the highest frequency
    for letter, frequency in frequency_map.items():
        if frequency == highest_frequency:
            common_letters.add(letter)

    return common_letters, highest_frequency

# main function of finding the most common letter in a list of words
def most_common_letters(words):
    letter_frequencies = count_letter_frequencies(words)
    most_common, max_count = find_most_common_letters(letter_frequencies)
    return most_common, max_count

# Example usage
word_collection = ["fewer","drest","fuzes","porae","moose","feuar","zoppo","piing","sesey","acted","imino"]

most_common_chars, occurrence_count = most_common_letters(word_collection)

# Displaying results
print("Most common letter : ")
print(f" {most_common_chars}, appearing {occurrence_count} times.")
