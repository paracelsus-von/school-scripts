from collections import Counter
import glob
import os
import io

directory = raw_input("Directory of files to analyse: ")
if directory == "":
    directory = "C:/Users/jacob/OneDrive/Documents/GitHub/school-scripts/wordcounter"

text = []

os.chdir(directory)
for filename in glob.glob("*.txt"):

    file_open = open(filename, "r")

    # Creating list of words to ignore
    bad_words = ["m:", "f:", "questions", "recording", "question", "number", "the", "answer"]
    bad_words += ["read", "write", "minutes", "this", "test", "and", "any", "time", "now"]
    bad_words += ["m2", "f2", "listen", "each", "ask", "and", "approcimately", "invigilator"]
    bad_words += ["during", "reading", "should", "pause", "pauses", "allowed", "secondary"]
    bad_words += ["allow", "including", "notes", "next", "about", "outside", "once"]
    bad_words += ["*", "*if", "restarted", "instructions", "information", "●", "b", "c"]
    bad_words += [str(x) for x in xrange(0,45)]
    bad_words += [str(x) for x in xrange(2000,2020)]
    bad_words += ["({})".format(letter) for letter in "abcdefghijklmnopqurstuvqxyz"]

    # Cleaning source text
    processed_text = map(str.lower, file_open.read().split())
    for char in [".", ",", "?", "!", "(", ")", "l'", "d'"]:
        processed_text = [x.strip(char) for x in processed_text]

    # Adding text frim each file to master text list
    text += processed_text

wordcount = Counter(text)

for item in sorted(wordcount.items(), key=lambda pair: pair[1], reverse=True):
    if item[0] not in bad_words and item[1] > 2 and "/" not in item[0] and "4" not in item[0] and "2" not in item[0]:
        print("{}\t{}".format(*item))

