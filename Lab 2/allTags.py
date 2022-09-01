import spacy

nlp = spacy.load("en_core_web_sm")

# All tags in spacy
for label in nlp.get_pipe("tagger").labels:
    print(label, " -- ", spacy.explain(label))