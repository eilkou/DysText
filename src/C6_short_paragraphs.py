import spacy

# Load spaCy model for sentence tokenization
nlp = spacy.load("en_core_web_sm")

def calculate_long_paragraph_score(text, ok_threshold=4, bad_threshold=6):
    """
    Calculate a score based on the number of sentences in each paragraph.

    :param text: The input text to analyze.
    :param ok_threshold: The threshold for considering a paragraph as "okay" (based on number of sentences).
    :param bad_threshold: The threshold for considering a paragraph as "bad" (based on number of sentences).
    :return: A dictionary with the percentage of long paragraphs and the overall score.
    """
    paragraphs = text.split("\n\n")  # Split text into paragraphs by double newlines
    paragraph_scores = []

    # Analyze each paragraph
    for paragraph in paragraphs:
        doc = nlp(paragraph)  # Process the paragraph using spaCy

        # Count the number of sentences in the paragraph
        num_sentences = len(list(doc.sents))

        # Score based on the number of sentences
        if num_sentences <= ok_threshold:
            score = 1  # Short paragraph
        elif ok_threshold < num_sentences <= bad_threshold:
            score = 0  # Medium paragraph
        else:
            score = -1  # Long paragraph

        paragraph_scores.append(score)

    # Calculate the percentage of positive scores (i.e., good paragraphs)
    good_paragraphs = paragraph_scores.count(1)
    total_paragraphs = len(paragraph_scores)

    # Handle division by zero if there are no paragraphs
    if total_paragraphs == 0:
        return {"Good Paragraph Percentage": 0, "Score": 0}

    # Calculate percentage of good paragraphs
    good_paragraph_percentage = (good_paragraphs / total_paragraphs) * 100

    # The overall score is the average of all paragraph scores
    overall_score = sum(paragraph_scores) / total_paragraphs

    return good_paragraph_percentage, overall_score
    # return {
    #     "Good Paragraph Percentage": good_paragraph_percentage,
    #     "Score": overall_score  # Average score for all paragraphs
    # }

# # Example usage:
# text = """This is a short paragraph.
# It has only a few sentences.
#
# This is a medium-length paragraph. It has more sentences, but it's not too long.
#
# This is a very long paragraph. It has a lot of sentences, making it quite long. We are testing whether the function will give it a negative score based on how many sentences it has.
#
# This is a very long paragraph. It has a lot of sentences, making it quite long. We are testing whether the function will give it a negative score based on how many sentences it has. This is a very long paragraph. It has a lot of sentences, making it quite long. We are testing whether the function will give it a negative score based on how many sentences it has.
#
# This is a very long paragraph. It has a lot of sentences, making it quite long. We are testing whether the function will give it a negative score based on how many sentences it has. This is a very long paragraph. It has a lot of sentences, making it quite long. We are testing whether the function will give it a negative score based on how many sentences it has. This is a very long paragraph. It has a lot of sentences, making it quite long. We are testing whether the function will give it a negative score based on how many sentences it has. This is a very long paragraph. It has a lot of sentences, making it quite long. We are testing whether the function will give it a negative score based on how many sentences it has.
#
# """

# result = calculate_long_paragraph_score(text)
# print(result)

def C6_score(text):
    good_paragraph_percentage, overall_score =calculate_long_paragraph_score(text)
    return overall_score
