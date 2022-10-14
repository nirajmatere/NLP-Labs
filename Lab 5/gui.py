import tkinter as tk
from tkinter import *
from nltk import word_tokenize
from collections import Counter
from collections import defaultdict
import re
import pandas as pd

top = tk.Tk()
top.title("NLP Lab 4")
top.geometry("1000x1000")

unknown_prob = 0.0000000000001
bigram_cnt = {}
unigram_cnt = {}
word_count = defaultdict(lambda: 0)
tag_word_count = Counter()
transition_probabilities = {}
emmission_probabilities = {}

def tag_word_counts(tagged_words):
        for  word,tag in tagged_words:
            word_count[word] += 1
            if (word,tag) in tag_word_count:
                tag_word_count[(word,tag)] += 1
            else:
                tag_word_count[(word,tag)] = 1
        return tag_word_count

def ngrams(text, n):
        Ngrams = []
        for i in range(len(text)): Ngrams.append(tuple(text[i: i + n]))
        return Ngrams

def bigram_counts(tags):
    for i_tag_bigram in ngrams(tags, 2):
        if i_tag_bigram in bigram_cnt:
            bigram_cnt[i_tag_bigram] += 1
        else:
            bigram_cnt[i_tag_bigram] = 1
    return bigram_cnt

def unigram_counts(tags):
    for tag in tags:
        if tag in unigram_cnt:
            unigram_cnt[tag] += 1
        else:
            unigram_cnt[tag] = 1
    return unigram_cnt

def clean(word):
        word = re.sub('\s+', '', word.lower())
        return word

def transition_probabilty(tags):
        bigrams = ngrams(tags, 2)
        # print(bigrams)
        for bigram in bigrams:
            if len(bigram)==2:
              transition_probabilities[bigram] = bigram_cnt[bigram]/ unigram_cnt[bigram[0]]
        return transition_probabilities

def emmission_probabilty(tagged_words):
        for word,tag in tagged_words:
            emmission_probabilities[word,tag] = tag_word_count[word,tag]/word_count[word]
        return emmission_probabilities

def print_matrix(dict0):
   
    data = list(zip(*dict0.keys())) + [dict0.values()]

    df = pd.DataFrame(zip(*data)).set_index([1,0])[2].unstack()
    
    df=df.fillna(0)
    AnswerBlock.insert(END, df)
    # print(df)

AnswerBlock = Text(top, height = 37, width = 115)
AnswerBlock.pack()

lines = open('corpus138.txt').readlines()

tagged_words = []
all_tags = []
AnswerBlock.insert(END, "\n************************Corpus*************************\n")
for sent in lines:
    word,tag=sent.split()
    if tag is None or tag in ['NIL']:
        continue
    all_tags.append(tag)
    word = clean(word)
    tagged_words.append((word,tag))
    if(word == 'eos'):
        AnswerBlock.insert(END,". ")
        continue
    AnswerBlock.insert(END, " ")
    AnswerBlock.insert(END, word)

AnswerBlock.insert(END, "\n\n")
AnswerBlock.insert(END, "\n************************Tags*************************\n")
for word in tagged_words:
    AnswerBlock.insert(END, " ")
    AnswerBlock.insert(END, word[0]) 
    AnswerBlock.insert(END, " (")
    AnswerBlock.insert(END, word[1])
    AnswerBlock.insert(END, ")")
    if(word[1] == 'eos'):
        AnswerBlock.insert(END, "\n")

AnswerBlock.insert(END, "\n")
tag_word_counts(tagged_words)
# print(tag_word_counts[0])
# print(tag_word_counts[1])
# print(tag_word_counts)
bigram_cnt = bigram_counts(all_tags)
print(bigram_cnt)
unigram_cnt = unigram_counts(all_tags)
print(unigram_cnt)
AnswerBlock.insert(END, "\n************************State Transition Probability Matrix*************************\n")
trans_mat=transition_probabilty(all_tags)
print_matrix(trans_mat)

AnswerBlock.insert(END, "\n")
AnswerBlock.insert(END, "\n************************Emission Probability Matrix*********************************\n")
emi_mat=emmission_probabilty(tagged_words)
print_matrix(emi_mat)
AnswerBlock.insert(END, "\n\n")

top.mainloop()