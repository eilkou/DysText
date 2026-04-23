import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')


def detect_double_negatives(doc):
    double_negatives = []
    double_negative_count = 0
    negative_prefixes = {"un", "in", "im", "dis", "ir"}  # Common prefixes indicating negation
    negative_words = {"no", "not", "never", "none", "nobody", "nothing", "nowhere"}  # Common negative words

    for sent in doc.sents:
        tokens = [token for token in sent]

        for i in range(len(tokens) - 1):
            # Check for "not" followed by a word with a negative prefix (e.g., "unlikely", "ungrateful")
            if tokens[i].text.lower() == "not":
                next_word = tokens[i + 1].text.lower()
                # Check if the next word has a negative prefix
                if any(next_word.startswith(prefix) for prefix in negative_prefixes):
                    double_negatives.append(sent.text)
                    double_negative_count += 1
                    break
            # Check for consecutive negative words (e.g., "no never", "not nothing")
            elif tokens[i].text.lower() in negative_words and tokens[i + 1].text.lower() in negative_words:
                double_negatives.append(sent.text)
                double_negative_count += 1
                break

    return double_negatives, double_negative_count


def C14_score(text):
    doc=nlp(text)
    double_negative_sentences, total_double_negatives = detect_double_negatives(doc)
    if total_double_negatives>0:
        print("-------------------------- DOUBLE NEGATIVES ---------------------")
        print("Double negatives detected in sentences:", double_negative_sentences)
    return max(-1, -total_double_negatives/5)


