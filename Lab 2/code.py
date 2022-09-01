import spacy
import pyinflect

nlp = spacy.load("en_core_web_sm")

verbs = input()
doc = nlp(verbs)

# All tags in spacy
# for label in nlp.get_pipe("tagger").labels:
#     print(label, " -- ", spacy.explain(label))


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
    possibilites = [token.text, base, gerund, ThirdPersonSingular, past_tense, past_participle, pluralNoun]
    print(possibilites)


# Output:
# eating - eat - eating - ate - eaten
# goes - go - going - went - gone
# touch - touch - touching - touched - touched
# felt - feel - feeling - felt - felt
# hit - hit - hitting - hit - hit
# sleeping - sleep - sleeping - slept - slept