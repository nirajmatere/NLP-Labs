import tkinter as tk
from tkinter import *
import spacy
import pyinflect

# Made By Niraj

#Logic Code Start

nlp = spacy.load("en_core_web_sm")

# verbs = input()
# doc = nlp(verbs)


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

#Logic Code End

#GUI Code Start

top = tk.Tk()
top.title("NLP Lab 2")
top.geometry("700x650")

possibilites = []

def Take_input():
    word = textInput.get("1.0", "end-1c")
    doc = nlp(word)
    for token in doc:
        base = token._.inflect("VB")
        if(base == None):
            base = token._.inflect("NN")
            if(base == None):
                base = token._.inflect("NNP")

        possibilites.append(base)

        gerund = token._.inflect("VBG")
        possibilites.append(gerund)

        ThirdPersonSingular = token._.inflect("VBZ")
        possibilites.append(ThirdPersonSingular)

        past_tense = token._.inflect("VBD")
        possibilites.append(past_tense)

        past_participle = token._.inflect("VBN")
        possibilites.append(past_participle)

        pluralNoun = token._.inflect("NNS")
        if(pluralNoun == None):
            pluralNoun = token._.inflect("NNPS")
        possibilites.append(pluralNoun)

        # print(token.text, "-", base, "-", gerund, "-", past_tense, "-", past_participle)
        # possibilites = [base, gerund, ThirdPersonSingular, past_tense, past_participle, pluralNoun]
        # print(possibilites)

    answerArray = []
    for name in possibilites:
        doc = nlp(name)
        col = []
        for token in doc:
            # print("Root : "+ token.lemma_)
            col.append(token.lemma_)

            tag = token.tag_
            # print("Category : "+ category(tag)) 
            col.append(category(tag))

            # print("Number : "+ getNum(tag))
            col.append(getNum(tag))

            # print("Tense : "+getTense(tag))
            col.append(getTense(tag))

            # print("Person : ")
            if(tag == "VBZ"):
                col.append("Third")
            elif(tag == "VBP"):
                col.append("Not Third")
            else:
                col.append("NA")

        answerArray.append(col)

    # print(answerArray[0])
    # print(answerArray[1])
    # print(answerArray[2])
    # print(answerArray[3])
    # print(answerArray[4])
    # print(answerArray[5])

label1 = Label(text = "Enter the word",font=("Courier", 17))
label1.pack()

textInput = Text(top, height = 1, width = 35)
textInput.pack()

button1 = Button(top, height = 2, width = 15, text ="Confirm Word", font=("Courier", 12), command = lambda:Take_input(),bg="Light Blue")
button1.pack()

#Set the Menu initially
menu= StringVar()
menu.set("Select Category")

#Create a dropdown Menu
drop = OptionMenu(top, menu,"Noun", "Verb","Adjective","Adverb")
drop.pack()


AnswerBlock = Text(top, height = 37, width = 55)
AnswerBlock.pack()

top.mainloop()

#GUI Code End