#!/usr/bin/python
import nltk
from nltk.corpus import wordnet as wn

user_input = raw_input("Start Typing")
    
def getsynsets(user_input):
    
        for synset in (wn.synsets(user_input)):
            try:
                print synset
                print synset.hypernyms() 
                print synset.hyponyms()
                print synset.meronyms()
                print synset.holonyms()
                print synset.part_meronyms()
                print synset.sister_terms()
                print synset.troponyms()
                print synset.derivationally_related_forms()
                print synset.inherited_hypernyms()
            except AttributeError as e: 
                print e
                pass
        

getsynsets(user_input)
