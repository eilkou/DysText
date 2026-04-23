import spacy
import numpy as np
from scipy.stats import norm

# Load spaCy model for sentence tokenization
nlp = spacy.load("en_core_web_sm")

def logarithmic_decay(x, mean, a, b, c):
    """
    Logarithmic decay function.
    - x: Sentence length
    - mean: Target mean length (60 for <60 characters, 70 for >70 characters)
    - a, b, c: Parameters to control the shape and smoothness of the curve.
    """
    if x <= c:  # Avoid log(0) or negative numbers
        return 0

    # Calculate the decay factor based on distance from the mean
    decay_score = a* np.log(b * (abs(x - mean) + c) + 1)

    return 1-decay_score

def calculate_short_sentence_score(text):
    """
    Calculate short sentence score based on sentence length in characters using a logarithmic decay function.
    - For sentences <60 characters, use a logarithmic distribution with mean=60.
    - For sentences >70 characters, use a logarithmic distribution with mean=70.
    - For sentences between 60 and 70 characters, return 1.

    :param text: The input text to analyze.
    :return: A dictionary with the calculated short sentence scores.
    """
    # Split text into sentences using spaCy
    doc = nlp(text)

    # Initialize a list to store scores
    sentence_scores = []

    # Logarithmic distribution parameters
    mean_less_60 = 60
    mean_greater_70 = 70
    a = 1  # Amplitude of the distribution
    b = 0.01  # Rate of decay (adjust for smoothness)
    c = 1  # Shifting constant to avoid issues with log(0)

    # Iterate over each sentence in the text
    for sent in doc.sents:
        sentence_length = sum(len(token.text) for token in sent if token.is_alpha)  # Count only alphabetic characters

        if sentence_length < 60:
            # Part 1: For sentences <60, calculate score using logarithmic decay (mean=60)
            score = logarithmic_decay(sentence_length, mean_less_60, a, b, c)
        elif sentence_length > 70 and sentence_length <= 100:
            # Part 2: For sentences >70, calculate score using logarithmic decay (mean=70)
            score = logarithmic_decay(sentence_length, mean_greater_70, a, b, c)
        elif sentence_length > 100:
            # Part 3: For sentences >100 characters, calculate decaying negative score, limited to -1
            score = max(-1, -b * (sentence_length - 100))  # Example decay: adjust factor to control the rate of decay
        else:
            # Part 4: For sentences between 60 and 70 characters, return score of 1
            score = 1
        # print(score)
        sentence_scores.append(score)

    # Calculate the overall short sentence score as the average of individual scores
    overall_score = sum(sentence_scores) if sentence_scores else 0
    score = overall_score / len(sentence_scores) if sentence_scores else 0

    return sentence_scores, score


def C7_score(text):
    sentence_scores, overall_score = calculate_short_sentence_score(text)
    return overall_score
