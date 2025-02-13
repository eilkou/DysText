import spacy
nlp = spacy.load("en_core_web_sm")


def active_voice_score(text):

    doc = nlp(text)

     # Count passive voice sentences
    passive_sentences = 0
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "auxpass" or token.dep_ == "nsubjpass":
                passive_sentences += 1
                break

    total_sentences = len(list(doc.sents))
    passive_percentage = (passive_sentences / total_sentences)
    active_score=1-passive_percentage
    print(
        "Passive Sentence Percentage", passive_percentage,
        "Active Voice Score", active_score
        )
    return active_score-passive_percentage

# text = """The papaer was made to be published in this venue. Please provide me with a question so I can give you an answer in bullet points! 😊  \n\nFor example, you could ask: \n\n* What are the benefits of exercise?\n* What are the main ingredients in a cake?\n* How do I change a tire? \n\n\nLet me know what you'd like to learn about! 🚀 \n"""
#
#
# print(active_voice_score(text))

def C8_score(text):
    return active_voice_score(text)
