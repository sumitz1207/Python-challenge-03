import os
import csv
#regex to find paragraph's setence lengths
import re

#create lists to store paragraph info
para_size = []
para_words = []
para_sent = []
para_val = []
#store user input to find text file to analyze
fileP = os.path.join(input("Please type your text file location: "))
with open(fileP, "r") as file:
    paragraph = file.read()
    #find word count by finding spaces
    para_words = (len(paragraph.split(" ")))
    #find paragraph char size by finding length of paragraph string
    para_size = len(paragraph)
    #find sentence length using regex on paragraph
    para_sent = len(re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", paragraph))
    #sentence length is the word count divided by sentence count
    sent_length = str(para_words/para_sent)
    #letter count is the size of the paragraph divided by the word count
    letter_count = str(para_size/para_words)
    #print out all paragraph analysis information
    print("\n")
    print("Paragraph Analysis")
    print("_________________________")
    print("Approx. Word Count: " + str(para_words))
    print("Approx. Sentence Count: " + str(para_sent))
    print("Average Letter Count: " + letter_count)
    print("Average Sentence Length: " + sent_length)

