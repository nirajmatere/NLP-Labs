import tkinter as tk
from tkinter import *
import spacy
import pyinflect

# Made By Niraj

#Logic Code Start

nlp = spacy.load("en_core_web_sm")

# verbs = input()
# doc = nlp(verbs)

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

#Logic Code End

#storing Input
def Calculate():
    flag = 0
    # AnswerBlock.insert(END, InputArray)
    # AnswerBlock.insert(END, '\n')
    # print("Printing Answer Array : ")
    # print(answerArray)
    # print("Printing Input Array : ")
    # print(InputArray)
    for x in answerArray:
        temp = x[0]
        # x[0] = str(x[0])
        # x = str(x)
        # print("Printing x : ")
        # print(x)
        # AnswerBlock.insert(END,  x)
        # AnswerBlock.insert(END, '\n')
        # AnswerBlock.insert(END, '\n')
        # AnswerBlock.insert(END, InputArray)
        # AnswerBlock.insert(END, '\n')
        # temp = list()
        # for p in x:
        #     temp.append(p)
        # equalityFlag = 0
        # for i in x:
        #     if(str(x[i]) != str(InputArray[i])):
        #         equalityFlag = 1
        # print(str(InputArray))
        # if(str(InputArray) == temp):
        #     print("Word : " + temp[0])

        count = 0
        for i in range(1,5):
            # print(x[i])
            # print(InputArray[i])
            if(x[i] == InputArray[i]):
                count = count+1

        # print("Printing Count: ")
        # print(count)
        if(count == 4):
            AnswerBlock.insert(END, "Best Suitable Word form of your Input is : " + str(temp))      
            AnswerBlock.insert(END, '\n')
           
            flag = 1

    if( flag == 0):
        AnswerBlock.insert(END, "Sorry ! No word exists with such features \n")    
        AnswerBlock.insert(END, "Try Different Options \n")  
        
    AnswerBlock.insert(END, '--------------------------------')
    AnswerBlock.insert(END, '\n')

#GUI Code Start

top = tk.Tk()
top.title("NLP Lab 2")
top.geometry("700x650")

possibilites = []

def Take_input():
    word = textInput.get("1.0", "end-1c")
    doc = nlp(word)

    InputArray.append(word)

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

    
    for name in possibilites:
        doc = nlp(name)
        col = []
        for token in doc:
            # print("Root : "+ token.lemma_)
            col.append(token)

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

button1 = Button(top, height = 1, width = 15, text ="Confirm Word", font=("Courier", 12), command = lambda:Take_input(),bg="Light Blue")
button1.pack()

#drop down inputs
def getInputCategory():
    Inputcategory = menu1.get()
    InputArray.append(Inputcategory)

def getInputNumber():
    InputNumber = menu2.get()
    InputArray.append(InputNumber)

def getInputTense():
    InputTense = menu3.get()
    InputArray.append(InputTense)

def getInputPerson():
    InputPerson = menu4.get()
    if(InputPerson == "First" or InputPerson == "Second"):
        InputPerson = "Not Third"
    
    InputArray.append(InputPerson)



#Category
#Set the Menu initially
menu1 = StringVar()
menu1.set("Select Category")

Inputcategory = ""

#Create a dropdown Menu
drop = OptionMenu(top, menu1,"Noun", "Verb","Adjective","Adverb")
drop.pack()

button3 = Button(top, height = 1, width = 15, text ="Confirm Category", font=("Courier", 12), command = lambda:getInputCategory(),bg="Light Blue")
button3.pack()

#Number
menu2 = StringVar()
menu2.set("Select Number")

InputNumber = ""

#Create a dropdown Menu
drop = OptionMenu(top, menu2,"Singular", "Plural","NA")
drop.pack()

button4 = Button(top, height = 1, width = 15, text ="Confirm Number", font=("Courier", 12), command = lambda:getInputNumber(),bg="Light Blue")
button4.pack()

#Tense
menu3 = StringVar()
menu3.set("Select Tense")

InputTense = ""

#Create a dropdown Menu
drop = OptionMenu(top, menu3,"Simple Present", "Simple Past","Simple Future","Present Continuos","Past Continuos", "Future Continuos","Present Participle","Past Participle", "Future Continuos")
drop.pack()

button2 = Button(top, height = 1, width = 15, text ="Confirm Tense", font=("Courier", 12), command = lambda:getInputTense(),bg="Light Blue")
button2.pack()

#Person
menu4= StringVar()
menu4.set("Select Person")

InputPerson = ""

#Create a dropdown Menu
drop = OptionMenu(top, menu4,"First", "Second","Third","NA")
drop.pack()

button2 = Button(top, height = 1, width = 15, text ="Confirm Person", font=("Courier", 12), command = lambda:getInputPerson(),bg="Light Blue")
button2.pack()


button2 = Button(top, height = 2, width = 15, text ="Get Result", font=("Courier", 12), command = lambda:Calculate(),bg="Light Blue")
button2.pack()


AnswerBlock = Text(top, height = 37, width = 55)
AnswerBlock.pack()

top.mainloop()

#GUI Code End