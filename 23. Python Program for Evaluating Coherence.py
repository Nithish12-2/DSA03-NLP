from transformers import pipeline

# Load a model for evaluating text coherence
coherence_model = pipeline("text-classification", model="roberta-base")

def evaluate_coherence(text):
    result = coherence_model(text)
    return result

text = "I went to the store. I bought apples. It was a great day."
coherence_score = evaluate_coherence(text)
print(coherence_score)
