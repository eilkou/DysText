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


def C11_score(text):
    return active_voice_score(text)
