import spacy
import re

# Load spaCy model for named entity recognition
nlp = spacy.load("en_core_web_sm")

def detect_uppercase_chars_excluding_names_locations(text):
    """
    Detects uppercase characters in the middle of sentences, excluding proper names and locations.
    :param text: The input text to analyze.
    :return: A tuple containing:
        - A list of uppercase characters found (excluding names and locations).
        - The total count of uppercase characters.
    """
    # Process the text with spaCy to extract named entities
    doc = nlp(text)

    # Identify all named entities (persons, locations, etc.)
    # We'll use the entity text in lowercase form for comparison
    named_entities = set()

    # Collect named entities (including multi-word entities)
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'GPE', 'LOC']:  # PERSON for names, GPE for locations
            # Store the entire named entity as lowercase (multi-word support)
            named_entities.add(ent.text.lower())

    # Split text into paragraphs by double newlines (empty lines)
    paragraphs = text.split("\n\n")

    # List to hold uppercase characters found in the middle of sentences
    uppercase_chars = []

    # Regular expression patterns for itemizations, quotes, and backticks
    itemization_pattern = r'^\s*[A-Za-z]\.[\s|\)]'  # Matches itemizations like "A.", "I.", "1."

    # Matches words enclosed in quotes, backticks, or smart quotes
    quote_pattern = r'[`\'"\“\”‘’]([^`\'"\“\”‘’]+)[`\'"\“\”‘’]'

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue  # Skip empty paragraphs

        # Split paragraph into sentences using regex, keeping punctuation marks
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)

        first_word_skipped = False  # To track first word after an empty line

        for sentence in sentences:
            sentence = sentence.strip()

            # Skip if sentence matches itemization pattern (e.g., "I." or "1.")
            if re.match(itemization_pattern, sentence):
                continue

            # Split sentence into words
            words = sentence.split()

            # Skip first uppercase character in a sentence or paragraph
            sentence_started = False

            for i, word in enumerate(words):
                # Skip the first word after an empty line
                if not first_word_skipped:
                    first_word_skipped = True
                    continue  # Skip this iteration

                # If word starts with a quote (check for both normal and smart quotes)
                if word[0] in ['`', "'", '"', '“', '”', '‘', '’']:
                    # Remove surrounding quotes
                    word = word.strip('`"\“\”\'‘’')

                # Skip if the word is within quotes or backticks (after quote removal)
                if re.search(quote_pattern, word):
                    continue

                for char_idx, char in enumerate(word):
                    if char.isupper():

                        # Skip if the uppercase character is part of a name or location
                        clean_word = re.sub(r'[^\w\s]', '', word).lower()  # Remove punctuation

                        # Check if the word is part of a named entity
                        if clean_word not in named_entities:
                            # Skip the first uppercase letter of a sentence
                            if sentence_started or char_idx > 0:
                                uppercase_chars.append(word)

                            # Mark that sentence has started to avoid first letter in sentence
                            if not sentence_started and char_idx == 0:
                                sentence_started = True

    # Return the list of uppercase characters and their count
    return uppercase_chars, len(uppercase_chars)


def C5_score(text):
    uppercase_chars, count = detect_uppercase_chars_excluding_names_locations(text)
    if count>0:
        print('------------------- UPPERCASES -------------------')
        print("Uppercases found:")
        print(uppercase_chars)
        return -1
    return 0
