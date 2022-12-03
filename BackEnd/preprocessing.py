# Load your usual SpaCy model (one of SpaCy English models)
import coreferee
import spacy
nlp = spacy.load('en_core_web_sm')


# Add coreferee to SpaCy's pipe
nlp.add_pipe('coreferee')


# You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
Passenger_Info = '''Andrew boarded the Titanic at Southampton as a second class passenger (ticket number 34050, which cost £10, 10s) 
          and was bound for the mining region of Houghton, Michigan. During the voyage he shared a dining table with Edwina 
          Troutt, Edgar Andrew, Charles and Alice Louch, Jacob Milling and Bertha Ilett.'''


Passenger_Info.rstrip()

doc = nlp(Passenger_Info)
triples = []
sub = ''
rel = ''
obj = ''

subjectTags = ['nsubj', 'nsubjpass', 'csubj', 'csubjpass',
               'agent', 'expl']
objectTags = ['dobj', 'dative', 'attr', 'oprd']
conjTags = ['conj']

for token in doc:
    #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
    #print(token.lemma_, token.pos_, token.tag_)
    pass

# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)
#     print(ent.text, ent.lemma_, ent.label_)
#     pass
print()


# CHUNK and INGDEPENDENCY PARSING 
for chunk in doc.noun_chunks:
    print(chunk.text, '|', chunk.root.text, '|',
          chunk.root.dep_, '|', chunk.root.head.text)
    if chunk.root.dep_ in subjectTags:
        sub = chunk.text
        #rel = chunk.root.head.text
        obj = ''
    elif chunk.root.dep_ in objectTags:
        rel = chunk.root.head.text
        obj = chunk.text
        if sub:
            triples.append((sub, rel, obj))
    elif chunk.root.dep_ in conjTags:
        if rel and sub:
            triples.append((sub, rel, chunk.text))
    elif chunk.root.dep_ == 'pobj':
        if sub and rel:
            triples.append((obj, chunk.root.head.text, chunk.text))
print()
for x in triples:
    print(x)
print()

# COREF RESOLUTION
for x in doc._.coref_clusters:
    print(x)