import os
import re

filename = 'Resources/paragraph_2.txt'

with open(filename, 'r') as textfile:
    lines = textfile.read().replace('\n', ' ')

words = lines.split(" ")
sentences = re.split("(?<=[.\"!?]) +", lines)
total_characters_pw = 0

for word in words:
    total_characters_pw += len(word)

total_characters_ps = 0

for sentence in sentences:
    total_characters_ps += len(sentence)
     
print("Paragraph Analysis")
print("--------------------")
print("Approximate Word Count: {}".format(len(words)))
print("Approximate Sentence Count: {}".format(len(sentences)))
print("Approximate Letter Count: {}".format(total_characters_pw / len(words)))
print("Average Sentence Length: {}".format(total_characters_ps / len(sentences)))
    
