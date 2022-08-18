import tkinter as tk
from tkinter import *
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy

nlp = spacy.load("en_core_web_sm")

def category(tags):
    if(tags=='VB'or tags=='VBP'or tags=='VBZ' or tags=='VBD' or tags=='VBN' or tags=='VBG'):
        return "Verb"
    elif(tags=='NN'or  tags=='NNS' or tags=='NNP'or tags=='NNPS'):
        return "Noun"
    elif(tags=='PRP' or tags=='PRP$' or tags=='WP' or tags=='WP$'):
        return "Pronoun"
    elif(tags=='RBS' or tags=='RBR' or tags=='RB' or tags=='WRB'):
        return "Adverb"
    elif(tags=='TO'or tags=='IN'):
        return "Preposition"
    elif(tags=='CC'):
        return "Conjunction"
    else:
        return "NA"
    
def getNum(tags):
    if(tags=='NNS' or tags=='NNPS' ):
        return "Plural"
    elif(tags=='NN' or tags=='NNP' or tags=='VB' or tags=='VBZ'):
        return "Singular"
    else:
        return "NA"
 
def getTense(tags):
    if(tags=='VB' or tags=='VBP' or tags=='VBZ'):
        return "Simple Present"
    elif(tags=='VBC' or tags=='VBF'):
        return "Simple Future"
    elif(tags=='VBD'):
        return "Simple Past"
    elif(tags=='VBG'):
        return "Present Participle"
    elif(tags=='VBN'):
        return "Past Participle"
    else:
        return "NA"

top = tk.Tk()
top.title("NLP Lab 1")
top.geometry("700x650")
name_var=tk.StringVar()
passw_var=tk.StringVar()

def Take_input():
    word = textInput.get("1.0", "end-1c")
    doc = nlp(word)
	
    firstItr = True
    for token in doc:
        AnswerBlock.insert(END, "Word : " + word)
        AnswerBlock.insert(END, '\n')
        AnswerBlock.insert(END, "Root : " + token.lemma_)
        AnswerBlock.insert(END, '\n')
        AnswerBlock.insert(END, "Category : " + category(token.tag_))
        AnswerBlock.insert(END, '\n')
        AnswerBlock.insert(END, "Number : " + getNum(token.tag_))
        AnswerBlock.insert(END, '\n')
        AnswerBlock.insert(END, "Tense : " + getTense(token.tag_))
        AnswerBlock.insert(END, '\n')
        AnswerBlock.insert(END, '--------------------------------')
        AnswerBlock.insert(END, '\n')


label1 = Label(text = "Enter the word",font=("Courier", 17))
label1.pack()

textInput = Text(top, height = 1, width = 35)
textInput.pack()

button1 = Button(top, height = 2, width = 15, text ="Get Result", font=("Courier", 12), command = lambda:Take_input(),bg="Light Blue")
button1.pack()

AnswerBlock = Text(top, height = 37, width = 55)
AnswerBlock.pack()




top.mainloop()