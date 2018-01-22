from collections import Counter
import glob
import os
import io
import csv

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
    for char in [".", ",", "?", "!", "(", ")", "*", "+", "l'", "d'"]:
        processed_text = [x.strip(char) for x in processed_text]

    # Adding text frim each file to master text list
    text += processed_text

wordcount = Counter(text)
sorted_wordcount = sorted(wordcount.items(), key=lambda pair: pair[1], reverse=True)
sorted_wordcount_clean = []

for item in sorted_wordcount:
    if item[0] not in bad_words and item[1] > 2 and "/" not in item[0] and "4" not in item[0] and "3" not in item[0] and "2" not in item[0] and len(item[0])>0:
        sorted_wordcount_clean.append(item)
        print("{}\t{}".format(*item))

answer = raw_input("\n\n-----------------\n\nDo you want to save this as a .csv file?")

if answer.lower() != "no":
    with open('word_count.csv','wb') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['word','frequency'])
        for row in sorted_wordcount_clean:
            csv_out.writerow(row)