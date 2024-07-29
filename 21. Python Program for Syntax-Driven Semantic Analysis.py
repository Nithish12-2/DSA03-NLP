import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases(sentence):
    doc = nlp(sentence)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    meanings = [chunk.root.dep_ for chunk in doc.noun_chunks]
    return list(zip(noun_phrases, meanings))

sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases_meanings = extract_noun_phrases(sentence)
print(noun_phrases_meanings)
