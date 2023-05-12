import nltk
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import myBinarySearch
import legal

sentence_server = sys.argv[1]
f1 = open("tc.txt", "w", encoding="utf8")
f1.write(sentence_server)
f1.close()

open("tc2.txt", "w").close()

# new--------------
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
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.0 * average)):
        summary += " " + sentence
# print(summary)
sys.stdout.flush()

f2 = open("tc2.txt", "w", encoding="utf8")
f2.write(summary)
f2.close()


# new --------------------

# old----------------------------------------------
# f = open("tc.txt", "r")
# file = f.read()

# # Plain text parsers since we are parsing through text
# from sumy.parsers.plaintext import PlaintextParser

# # for tokenization
# from sumy.nlp.tokenizers import Tokenizer

# # name of the plain-text file ~ bbc news dataset
# Language = "english"
# parser = PlaintextParser.from_file("tc.txt", Tokenizer(Language))

# from sumy.summarizers.lex_rank import LexRankSummarizer

# summarizer = LexRankSummarizer()
# # Summarize the document with 2 sentences
# summary = summarizer(parser.document, 3)


# for sentence in summary:
#     print(sentence)
# sys.stdout.flush()

# old-------------------------------------------
