import spacy
from spacy.tokens import Span

# Load spaCy model with coreference resolution capabilities
nlp = spacy.load("en_coref_sm")

def resolve_references(text):
    doc = nlp(text)
    return [(ent.text, ent._.coref_clusters) for ent in doc.ents]

text = "John went to the store. He bought some apples."
resolved_references = resolve_references(text)
print(resolved_references)
