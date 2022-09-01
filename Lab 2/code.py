import spacy
import pyinflect

nlp = spacy.load("en_core_web_sm")

verbs = input()
doc = nlp(verbs)

for token in doc:
    base = token._.inflect("VB")
    if(base == None):
        base = token._.inflect("NN")
        if(base == None):
            base = token._.inflect("NNP")

    gerund = token._.inflect("VBG")
    ThirdPersonSingular = token._.inflect("VBZ")
    past_tense = token._.inflect("VBD")
    past_participle = token._.inflect("VBN")
    pluralNoun = token._.inflect("NNS")
    if(pluralNoun == None):
         pluralNoun = token._.inflect("NNPS")

    # print(token.text, "-", base, "-", gerund, "-", past_tense, "-", past_participle)
    possibilites = [base, gerund, ThirdPersonSingular, past_tense, past_participle, pluralNoun]
    print(possibilites)


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

print(answerArray[0])
print(answerArray[1])
print(answerArray[2])
print(answerArray[3])
print(answerArray[4])
print(answerArray[5])

# Output:
# eating - eat - eating - ate - eaten
# goes - go - going - went - gone
# touch - touch - touching - touched - touched
# felt - feel - feeling - felt - felt
# hit - hit - hitting - hit - hit
# sleeping - sleep - sleeping - slept - slept