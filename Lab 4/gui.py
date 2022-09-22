import tkinter as tk
from tkinter import *
from nltk import word_tokenize

top = tk.Tk()
top.title("NLP Lab 4")
top.geometry("700x650")

def preprocess(d):
    d=d.lower()
    d="eos "+ d
    d=d.replace("."," eos")
    return d
def generate_tokens(d):
    tokens = word_tokenize(d)
    return tokens
def generate_tokens_freq(tokens):
    dct={}
    for i in tokens:
        dct[i]=0
    for i in tokens:
        dct[i]+=1
    return dct
def generate_ngrams(tokens,k):
    l=[]
    i=0
    while(i<len(tokens)):
        l.append(tokens[i:i+k])
        i=i+1
    l=l[:-1]
    return l
def generate_ngram_freq(bigram):
    dct1={}
    for i in bigram:
        st=" ".join(i)
        dct1[st]=0
    for i in bigram:
        st=" ".join(i)
        dct1[st]+=1
    return dct1
def find1(s,dct1):
    try:
        return dct1[s]
    except:
        return 0.1
def print_probability_table(distinct_tokens,dct,dct1):
    n=len(distinct_tokens)
    l=[[]*n for i in range(n)]
    for i in range(n):
        denominator = dct[distinct_tokens[i]]
        for j in range(n):
            numerator = find1(distinct_tokens[i]+" "+distinct_tokens[j],dct1)
            l[i].append(float("{:.3f}".format(numerator/denominator)))
    return l

    
d = "My  name is Niraj Matere. I am studying in IIIT Nagpur. I love playing football. Football is my favorite game. This is NLP lab 4. A week has seven days. Sun rises from East. Today is rainy day. Yesterday was sunny. I am listening to the songs.Cricket is very popular sport, especially in India. India is big country. I love India." 

d = preprocess(d)

tokens=generate_tokens(d)

distinct_tokens = list(set(sorted(tokens)))

dct=generate_tokens_freq(tokens)

bigram = generate_ngrams(tokens,2)

dct1=generate_ngram_freq(bigram)

probability_table=print_probability_table(distinct_tokens,dct,dct1)

n=len(distinct_tokens)


def Take_input():
    text = textInput.get("1.0", "end-1c")
    AnswerBlock.insert(END, "Given Text : " + text)
    AnswerBlock.insert(END, '\n')
    AnswerBlock.insert(END, '\n')

    p = preprocess(text)

    t=generate_tokens(p)

    n = generate_ngrams(t,2)

    s=1 
    dct2={}
    for i in n:
        dct2[" ".join(i)]=0
    
    for i in n:
        try:
            k=distinct_tokens.index(i[0])
            m=distinct_tokens.index(i[1])
            dct2[" ".join(i)]=probability_table[k][m]
            AnswerBlock.insert(END, "P('{}')\t=  " .format(' '.join(i)),probability_table  [k][m])
            AnswerBlock.insert(END, probability_table  [k][m])
            # print("P('{}')\t=  ".format(' '.join(i)),probability_table  [k][m])
            s*=probability_table[k][m]
            AnswerBlock.insert(END, '\n')
        except:
            AnswerBlock.insert(END, "Anyone or more of the enterred words are not in the database. Please try another sentence. \n")
            AnswerBlock.insert(END, '\n------------------------------------------------------\n')

            return

    AnswerBlock.insert(END, '\n')
    AnswerBlock.insert(END, "Calculate Probability of the sentence : \n")      
    # print("\n"+'\033[1m'+ "Calculate Probability of the sentence"+'\033[0m')
    AnswerBlock.insert(END, '\n')
    AnswerBlock.insert(END, f"P('{text}') \n=")      
    # print(f"P('{text}') \n= ",end="")
    x=dct2.popitem()
    for i in dct2:
        AnswerBlock.insert(END, f" P('{i}') *" )
        # AnswerBlock.insert(END, '\n')
        # print(f"P('{i}')", end=" * ")
    AnswerBlock.insert(END, f"P('{x[0]}')\n= ")
    # AnswerBlock.insert(END, '\n')
    # print(f"P('{x[0]}')\n= ", end='')

    for i in dct2:
        AnswerBlock.insert(END, dct2[i])
        AnswerBlock.insert(END, ' * ')
        # AnswerBlock.insert(END, '\n')
        # print(dct2[i], end=" * ")
    AnswerBlock.insert(END, x[1], " = ")
    AnswerBlock.insert(END, "\n= ")
    AnswerBlock.insert(END, s)
    # print(x[1],"\n=",s)

    AnswerBlock.insert(END, '\n')
    AnswerBlock.insert(END, '\n')
    AnswerBlock.insert(END, f"Probability('{text}') = "+"{:.5f}".format(s))
    # AnswerBlock.insert(END, '\n')
    # print("\n"+'\033[1m'+f"Probability('{text}') = "+"{:.5f}".format(s))
    AnswerBlock.insert(END, '\n------------------------------------------------------\n')


label1 = Label(text = "Enter text to check its probability",font=("Courier", 17))
label1.pack()

textInput = Text(top, height = 1, width = 35)
textInput.pack()

button1 = Button(top, height = 2, width = 15, text ="Get Result", font=("Courier", 12), command = lambda:Take_input(),bg="Light Blue")
button1.pack()

AnswerBlock = Text(top, height = 37, width = 115)
AnswerBlock.insert(END, '\t\t\t\t\t--------- Smoothing Factor = 0.1 ---------\t\n\n')
AnswerBlock.pack()

top.mainloop()