import collections
import re
import string
from collections import Counter

###Frequency of characters
def char_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # Create a dictionary to store the frequency of each character
        ch_frequency = collections.Counter(text)
        # Sort the dictionary by value in descending order
        sorted_ch_frequency = sorted(ch_frequency.items(), key=lambda x: x[1], reverse=True)
        # Print the first five characters
        for i in range(5):
            print(sorted_ch_frequency[i][0], sorted_ch_frequency[i][1])

def word_status(file_path):
    with open(file_path,'r') as f:
        text=f.read()
        text=text.lower()
        words = text.split()
        word_status = Counter(words)
        sorted_words = sorted(word_status.items(), key=lambda x: x[1], reverse=True)
        for word, frequency in sorted_words:
            print(f'{word} : {frequency}')

##character read frequency
char_frequency("read.txt")
##word read frequency
word_status('read.txt')
