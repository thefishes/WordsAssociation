#!/usr/bin/python
import nltk
from nltk.corpus import wordnet as wn

user_input = raw_input("Start Typing")

    
def getsynsets(user_input):
    
        for synset in (wn.synsets(user_input)):
            print synset
            nyms = ['hypernyms', 'hyponyms', 'meronyms', 'holonyms', 'part_meronyms', 'sisterm_terms', 'troponyms', 'inherited_hypernyms']
            for i in nyms:
                try:
                    print getattr(synset, i)()
                except AttributeError as e: 
                    print e
                    pass

        for lemma in (wn.lemmas(user_input)):
            print lemma
            lemmanyms = ['antonyms', 'derivationally_related_forms', 'pertainyms']
            for y in lemmanyms:
                try:
                    print getattr(lemma, y)()
                except AttribureError as e:
                    print e
                    pass


getsynsets(user_input)


