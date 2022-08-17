from tkinter import *
import nltk
import spacy
import gender_guesser.detector as gender
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
nlp = spacy.load("en_core_web_sm")
d = gender.Detector()
root = Tk()
root.geometry( "800x800" )

def category(tags):
    if(tags=='VB'or tags=='VBP'or tags=='VBZ' or tags=='VBD' or tags=='VBN' or tags=='VBG'):
        return "Verb"
    elif(tags=='NN'or  tags=='NNS' or tags=='NNP'or tags=='NNPS'):
        return "Noun"
    elif(tags=='PRP' or tags=='PRP$' or tags=='WP' or tags=='WP$'):
        return "Pronoun"
    elif(tags=='RBS' or tags=='RBR' or tags=='RB' or tags=='WRB'):
        return "adverb"
    elif(tags=='TO'or tags=='IN'):
        return "Preposition"
    elif(tags=='CC'):
        return "Conjunction"
    else:
        return "Na"
       
def getNum(tags):
    if(tags=='NNS' or tags=='NNPS' ):
        return "Plural"
    elif(tags=='NN' or tags=='NNP' or tags=='VB' or tags=='VBZ'):
        return "Singular"
    else:
        return "Na"

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
        return "Na"

 #[root,category,gender,number,person,case,tense] 
def show():
    word_list=[clicked.get()]
    tag=nltk.pos_tag(word_list)
    doc=nlp(clicked.get())
    label0.config( text = "Word:  "+clicked.get())
   # for token in doc:
    label1.config( text = "Root:  "+ lemmatizer.lemmatize(clicked.get()) ) #token.lemma_)                #
    label2.config( text = "Category:  "+category(tag[0][1]))
    label3.config( text = "Gender:  "+d.get_gender(clicked.get()))
    label4.config( text = "Number:  "+getNum(tag[0][1]))
    #label5.config( text = "Person:  "+getPerson(tag[0][1]))
    label6.config( text = "Case:  "+"Na")
    label7.config( text = "Tense:  "+getTense(tag[0][1]))


options = [
    "plays",
    "playing",
    "runs",
    "running",
    "study",
    "studies",
    "studying",
    "children",
    "hosting",
    "started",
    "accepts",	
    "acceptance",
    "boys",
    "happinesses",
    "beatings",
    "beats"

]
  
# datatype of menu text
clicked = StringVar()
clicked.set( "---Select word---" )
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "Get answer" , command = show ).pack()
  
# Create Labels
label0 = Label( root , text = " " )
label1 = Label( root , text = " " )
label2 = Label( root , text = " " )
label3 = Label( root , text = " " )
label4 = Label( root , text = " " )
label5 = Label( root , text = " " )
label6 = Label( root , text = " " )
label7 = Label( root , text = " " )
label0.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
root.mainloop()