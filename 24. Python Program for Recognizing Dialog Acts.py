from transformers import pipeline

# Load a dialog act classification model
dialog_act_model = pipeline("text-classification", model="bert-base-uncased")

def classify_dialog_act(dialogue):
    result = dialog_act_model(dialogue)
    return result

dialogue = "Can you help me with this task?"
dialog_act = classify_dialog_act(dialogue)
print(dialog_act)
