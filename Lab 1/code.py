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


# print("Enter the word:")
# word=input()
# print("Word : "+word)

def getAnswer(name):
    doc = nlp(name)
    #[root,category,gender,number,person,case,tense]
    for token in doc:
        print("Root : "+ token.lemma_)
        tag = token.tag_
        print("Category : "+ category(tag)) 
        print("Number : "+ getNum(tag))
        print("Tense : "+getTense(tag))


# doc = nlp(word)
# getAnswer(doc)