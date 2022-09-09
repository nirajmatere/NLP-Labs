from ast import Delete
import tkinter as tk
from tkinter import *
import spacy
import pyinflect

# Made By Niraj

nlp = spacy.load("en_core_web_sm")

top = tk.Tk()
top.title("NLP Lab 2")
top.geometry("700x650")

possibilites = list()
InputArray = list()
answerArray = list()

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


def Calculate():
    rootWord = str(possibilites[0])
    # print(rootWord)
    s = {rootWord}
    # s.update(possibilites)
    # print(s)
    for x in possibilites:
        if(x != None and x[0][0] == rootWord[0]):
            s.add(x)
            # AnswerBlock.insert(END, "Morphological Form : " + str(x))      
            # AnswerBlock.insert(END, '\n')
    
    
    for val in s:
        AnswerBlock.insert(END, "Morphological Form : " + val)      
        AnswerBlock.insert(END, '\n')
    AnswerBlock.insert(END, '--------------------------------')
    AnswerBlock.insert(END, '\n')


def Take_input():
    word = textInput.get("1.0", "end-1c")
    doc = nlp(word)

    InputArray.append(word)

    for token in doc:
        # print(token)
        # print(token.tag_)
        base = token._.inflect("VB")
        if(base == None):
            base = token._.inflect("NN")
            if(base == None):
                base = token._.inflect("NNP")

        # print(base)
        possibilites.append(base)

        gerund = token._.inflect("VBG")
        # print(gerund)
        possibilites.append(gerund)

        ThirdPersonSingular = token._.inflect("VBZ")
        # print(ThirdPersonSingular)
        possibilites.append(ThirdPersonSingular)

        past_tense = token._.inflect("VBD")
        # print(past_tense)
        possibilites.append(past_tense)

        past_participle = token._.inflect("VBN")
        # print(past_participle)
        possibilites.append(past_participle)

        adverb = token._.inflect("RB")
        # print("adverb : " + str(adverb))
        possibilites.append(adverb)
        
        adverbS = token._.inflect("RBS")
        # print(adverbS)
        possibilites.append(adverbS) 

        adverbP = token._.inflect("RBR")
        # print(adverbP)
        possibilites.append(adverbP)

        adjective = token._.inflect("JJ")
        # print(adjective)
        possibilites.append(adjective)
        
        adjectiveS = token._.inflect("JJS")
        # print(adjectiveS)
        possibilites.append(adverbS) 

        adjectiveP = token._.inflect("JJS")
        # print(adjectiveP)
        possibilites.append(adjectiveP)

        POSW = token._.inflect("POS")
        # print(POSW)
        possibilites.append(POSW)

        affix = token._.inflect("AFX")
        # print(affix)
        possibilites.append(affix)

        if(token.tag_ != "VB" and token.tag_ != "VBZ" and token.tag_ != "VBD" and token.tag_ != "VBN" and token.tag_ != "VBG"):
            pluralNoun = token._.inflect("NNS")
            if(pluralNoun == None):
                pluralNoun = token._.inflect("NNPS")      
            possibilites.append(pluralNoun)

    rootWord = word
    # print(rootWord)
    s = {rootWord}
    # s.update(possibilites)
    # print(s)

    for x in possibilites:
        if(x != None and x[0][0] == rootWord[0]):
            s.add(x)
            # AnswerBlock.insert(END, "Morphological Form : " + str(x))      
            # AnswerBlock.insert(END, '\n')
    
    for val in s:
        AnswerBlock.insert(END, "Morphological Form : " + val)      
        AnswerBlock.insert(END, '\n')

    AnswerBlock.insert(END, '--------------------------------')
    AnswerBlock.insert(END, '\n')
        # print(token.text, "-", base, "-", gerund, "-", past_tense, "-", past_participle)
        # possibilites = [base, gerund, ThirdPersonSingular, past_tense, past_participle, pluralNoun]
        # print(possibilites)
    
    possibilites.clear()

label1 = Label(text = "Enter the word",font=("Courier", 17))
label1.pack()

textInput = Text(top, height = 1, width = 35)
textInput.pack()

button1 = Button(top, height = 2, width = 15, text ="Get Result", font=("Courier", 12), command = lambda:Take_input(),bg="Light Blue")
button1.pack()

# button2 = Button(top, height = 2, width = 15, text ="Get Result", font=("Courier", 12), command = lambda:Calculate(),bg="Light Blue")
# button2.pack()

AnswerBlock = Text(top, height = 37, width = 55)
AnswerBlock.pack()

top.mainloop()