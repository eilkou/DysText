import nltk
import syllapy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.corpus import words, cmudict

# Download necessary NLTK resources
nltk.download('punkt_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('cmudict')

# Initialize the CMU Pronouncing Dictionary for syllable counting
d = cmudict.dict()

# Function for calculating Flesch-Kincaid Reading Ease Score
def flesch_kincaid_reading_ease(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Count syllables
    syllables = sum(syllapy.count(word) for word in words if word.isalpha())

    # Calculate ASL and ASW
    ASL = len(words) / len(sentences)  # Average Sentence Length
    ASW = syllables / len(words)       # Average Syllables per Word

    # Flesch Reading Ease formula
    score = 206.835 - (1.015 * ASL) - (84.6 * ASW)
    return score

# Function for calculating simple language percentage based on readability score
def calculate_simple_language_percentage_using_readability(text):
    score = flesch_kincaid_reading_ease(text)
    # print(score/50-1)
    if score > 100:
         return 1  # Assume 100% simple if score is high (easier to read)
    return score/50 -1
    # # The readability score ranges from 0 to 100; higher is easier to read.
    # if score > 60:
    #     return 100  # Assume 100% simple if score is high (easier to read)
    # elif score > 50:
    #     return 70  # A bit complex but still mostly simple
    # elif score > 40:
    #     return 50  # Quite complex
    # else:
    #     return 30  # Very complex text

# Function for Part-of-Speech tagging method to calculate simple language percentage
def is_simple_word_pos(word, pos):
    """Assume simple words based on part-of-speech tagging."""
    if pos in ['NN', 'VB', 'JJ']:  # Nouns, Verbs, Adjectives
        return len(word) <= 5  # Simple words are usually 5 characters or less
    return False

def calculate_simple_language_percentage_using_pos(text):
    words_in_text = word_tokenize(text)
    tagged_words = pos_tag(words_in_text)

    # Count simple words based on POS tagging
    simple_words = [word for word, pos in tagged_words if is_simple_word_pos(word, pos)]

    # Calculate percentage of simple words
    simple_percentage = (len(simple_words) / len(words_in_text)) * 100 if words_in_text else 0
    # print(simple_percentage)
    return simple_percentage

# SWOG Classification Method
def is_simple_word_swog(word):
    """Classify words as SW (Simple Word) or OG (Other Group) based on length and commonality."""
    # Simple words are typically short and common
    if len(word) <= 6 and word.lower() in words.words():
        return True  # Simple Word (SW)
    else:
        return False  # Other Group (OG)

# Function to calculate percentage of SWOG in a text
def calculate_simple_language_percentage_using_swog(text):
    words_in_text = word_tokenize(text)

    # Filter out non-alphabetic words (remove punctuation)
    words_in_text = [word for word in words_in_text if word.isalpha()]

    # Count simple words (SW) using the SWOG classification
    simple_words = [word for word in words_in_text if is_simple_word_swog(word)]

    # Calculate percentage of simple words (SW)
    simple_percentage = (len(simple_words) / len(words_in_text)) * 100 if words_in_text else 0
    # print(simple_percentage)
    return simple_percentage

# Function to count syllables in a word using CMU dictionary
def count_syllables(word):
    """Return the number of syllables in a word."""
    word = word.lower()
    if word in d:
        # Return the max syllables in the word's possible pronunciations
        return max([len(list(y for y in x if y[-1].isdigit())) for x in d[word]])
    else:
        # If the word is not in the CMU dictionary, use a basic rule-based approach
        return len([char for char in word if char in "aeiou"])




# Function to calculate the Gunning Fog Index
def calculate_gunning_fog_index(text):
    sentences = sent_tokenize(text)  # Split the text into sentences
    words = word_tokenize(text)  # Split the text into words

    # Count the total number of words and sentences
    total_words = len(words)
    total_sentences = len(sentences)

    # Count complex words (words with 3 or more syllables)
    complex_words = [word for word in words if count_syllables(word) >= 3]
    complex_word_count = len(complex_words)

    # Calculate the Gunning Fog Index
    if total_sentences > 0 and total_words > 0:
        gunning_fog_index = 0.4 * ((total_words / total_sentences) + 100 * (complex_word_count / total_words))
        # print("Gunning Fox", gunning_fog_index)
        return gunning_fog_index
    else:
        return 0

# Function to scale GFI to a -1-1 range (higher = simpler language)
# # The function determines the "difficult" reading point to start above 14 gfi score
# def scale_gfi_to_100(gfi, max_gfi=14):
#     gfi = float(gfi)  # Ensure GFI is a float to avoid TypeError
#     if gfi>14:
#         return max(-1, 1 - gfi / max_gfi)  # Invert and scale to [-1,1]
#     return max(1, 1-gfi/max_gfi)

def scale_gfi_to_1(gfi, max_gfi=20):
    """
    Scale the Gunning Fog Index (GFI) to a range between -1 and 1,
    with a turning point at 14.
    - Scores below 14 will be scaled negatively from 0 to -1.
    - Scores above 14 will be scaled positively from 0 to 1.

    :param gfi: The Gunning Fog Index value.
    :param max_gfi: The maximum GFI value to consider for the positive scaling (default is 50).
    :return: A scaled GFI value between -1 and 1.
    """
    if gfi < 14:
        # Scale GFI <= 14 to a negative range [-1, 0]
        return (14 - gfi) / 14
    elif gfi > 14:
        # Scale GFI > 14 to a positive range [0, 1]
        return - (gfi - 14) / (max_gfi - 14)
    else:
        # If GFI == 14, the score is 0
        return 0

# Combined function to average both methods
def calculate_average_simple_language_percentage(text):
    # Get simple language percentages from both methods
    readability_percentage = calculate_simple_language_percentage_using_readability(text)
    gfi = calculate_gunning_fog_index(text)
    gfi_percentage = scale_gfi_to_1(gfi)
    # print(gfi_percentage)

    # Calculate the average
    average_percentage = (readability_percentage + gfi_percentage) / 2
    return average_percentage

# # Example usage
# text = """Ghana just like many other tropical countries is very much vulnerable to climate change and
# variability. An estimated 35 percent of the total land mass is desert and since the 1980s the
# has been increasing desertification of the northern part of the country. Desertification in
# Ghana is currently estimated to be proceeding at a rate of 20,000 hectares per annum
# thereby compromising water resource. n northern Ghana, these farmers are usually
# involved in the cultivation of staple grains including maize"""
# average_percentage = calculate_average_simple_language_percentage(text)
# print(f"Average Percentage of Simple Language: {average_percentage:.2f}%")

def C9_score(text):
    return calculate_average_simple_language_percentage(text)
