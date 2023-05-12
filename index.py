import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import myBinarySearch

import legal





f = open("tc.txt", "r", encoding="utf8")


text = f.read()

stopWords = set(stopwords.words("english"))

words = word_tokenize(text)
# print(words)

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()


def checker(word):
    if myBinarySearch.binary_search_string(legal.legal_words, word) != -1:
        return 3
    else:
        return 0


for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            val = checker(word)
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq + val
            else:
                sentenceValue[sentence] = freq + val

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]


average = int(sumValues / len(sentenceValue))

summary = ""
# change 2.5 to 1.2
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (2.5 * average)):
        summary += " " + sentence

print(summary)


# binarysearch
# import myBinarySearch

# arr = ["lol", "nk"]
# print(myBinarySearch.binary_search_string(arr, "nk"))
# print(legal.legal_words)
