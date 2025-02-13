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



    # # Split text into sentences using regex, keeping punctuation marks
    # sentences = re.split(r'(?<=[.!?])\s+', text)
    #
    # # List to hold uppercase characters found in the middle of sentences
    # uppercase_chars = []
    #
    # # Regular expression patterns for itemizations and quotes
    # itemization_pattern = r'^\s*[A-Za-z]\.[\s|\)]'  # Matches itemizations like "A.", "I.", "1."
    # quote_pattern =  r'[`\'"\“\”]([^`\'"\“\”]+)[`\'"\“\”]'  # Matches text within quotes or backticks
    #
    # # Iterate through sentences
    # for sentence in sentences:
    #     sentence = sentence.strip()
    #
    #     # Skip if sentence matches itemization pattern (e.g., "I." or "1.")
    #     if re.match(itemization_pattern, sentence):
    #         continue
    #
    #     # Split sentence into words
    #     words = sentence.split()
    #
    #     # Skip first uppercase character in a sentence
    #     sentence_started = False
    #
    #     for i, word in enumerate(words):
    #
    #         # If word starts with a quote (check for both normal and smart quotes) or I
    #         if word[0] in ['`', "'", '"', '“', '”', '‘', '’', '‘', 'I']:
    #             # If it's surrounded by quotes, we remove the quotes for further processing
    #             # word = word.strip('`"\“\”\'')  # Remove surrounding quotes
    #             continue
    #
    #         # Skip if the word is within quotes or backticks
    #         if re.search(quote_pattern, word):
    #             continue
    #
    #         for char_idx, char in enumerate(word):
    #             if char.isupper():
    #
    #                 # Skip if the uppercase character is part of a name or location
    #                 clean_word = re.sub(r'[^\w\s]', '', word).lower()  # Remove punctuation
    #
    #                 # Check if the word is part of a named entity
    #                 #if not any(clean_word == " ".join(named_entity) for named_entity in named_entities):
    #                 if clean_word not in named_entities:
    #                     # Skip the first uppercase letter of a sentence
    #                     if sentence_started or char_idx > 0:
    #                         uppercase_chars.append(word)
    #
    #                     # Mark that sentence has started to avoid first letter in sentence
    #                     if not sentence_started: #and char_idx == 0:
    #                         sentence_started = True
    #
    # # Return the list of uppercase characters and their count
    # return uppercase_chars, len(uppercase_chars)


# # Example usage:
# text = """
# Soil erosion is not a general problem in West Africa under indigenous husbandry systems. It
# is, however, locally a chronic problem, and in many areas a potential hazard under changing
# cultivation practices. Soil erosion is intimately associated with problems of water control
# and desertification, and it is thus convenient to consider both together.
#
# Over much of tropical Africa the annual water supply from precipitation is less than the
# amount of water most crop plants would transpire if adequately supplied with moisture.
# Furthermore, over much of this area the rainfall is unreliable in amount and occurrence,
# both seasonally and annually. Also it is commonly very intense. Thus conservation measures
# must involve efficient use of the available moisture, and the prevention of the adverse
# effect of intense rainfall, such as flash floods. A special section has been created in this
# chapter to discuss the drought at the Sahel region.
#
# Maintaining a plant cover and mulching, separately or together, constitute one approach to
# the problem, but the preservation of useless plants simply as a conservation measure
# involves the waste of moisture which might otherwise go the crop plant, and is feasible only
# in areas where the water supply is more or less adequate to the being grown. Mulching with
# dead plant matter is also not usually practicable, since there are other more pressing uses
# for such materials as straw, plant stems and leaves, which might be used for conservation of
# this type. Artificial mulches, such as bitumen-in-water, though practicable, are not usually
# economically or technically possible in the present socio-economic situation in areas where
# such measures are most needed.
#
# Contour and tie-ridging effectively achieve conservation of water supplies, and a diminution
# of runoff velocities. The combination of the two has proved their worth. These measures
# offer simple and satisfactory ways of controlling water use and preventing soil erosion, but
# soil differences still need to be taken into account. The importance of such measures cannot
# be overemphasized, and always involve major schemes of rehabilitation, embracing
# engineering works, afforestation, considerable modifications of traditional agricultural
# practices, even of settlement patterns and land apportionment. These imply considerable
# expense of money and of expertise which could otherwise be used for agricultural
# improvement, rather than for arresting the effects of past malpractices. Rainfall variability,
# and prolonged drought have been major environmental issues disturbing the African
# continent. On the more western part, while the Sahel region has had a long reputation of
# extreme drought conditions, most West-African countries have historically suffered from
# environmental challenges. For the past thirty years, inconsistencies in rainfall and high levels
# of variability have negatively affected agriculture. Rainfall provides the moist nature of soil
# and aids in its aeration encouraging massive agriculture production. Concerning rice
# production, it has had the tendency of causing fluctuations in production in countries like
# Sierra Leone and Gambia. The major climatic condition that has negatively impacted the
# agricultural activities of the West African regions is drought. This environmental
# phenomenon has persisted since the 1960s with the early 1980s and 70s witnessing the
# worst conditions of it. This drought had systematically altered the kind of food crops
# cultivated in the regions whiles drastically reducing the production of other crops. Examples
# include sorghum, millet and rice.In Gambia, farmers had claimed that, the droughts had
# altered the rains negatively. Rainfall in this country and other Sahelian states has being the
# main source of irrigational water for their crops. Considerably, Agricultural produce had
# increased in the 1950s and 60s due to the favourable rains in this period, however the late
# 1960s and early 70s saw the decline of the rains. In the southern part of the country,
# farmers claimed rains in the month June of the 70s were low comparing it to that of the
# 1950s. The rains in the latter had only last for a month. The major crop which has been
# affected by these droughts is rice. Rice has been the major staple of countries like Sierra
# Leone, Gambia and most Sahelian States. In Gambia about 20-30% of lands are converted to
# upland rice cultivation. Primarily, its production has been dominated by women serving as
# major source of income. Since the inception of this environmental phenomenon, rice
# production has declined approximately half of what use to be produced. This has led to
# most indigenes relying on exported ones. The major setback here is the reduced rains which
# has also in turn reduced run-off to the main lands of rice plantations. Generally, rivers have
# also dried due to this same issue.
#
# Other major staples which have been affected by the drought are millet, sorghum and
# groundnuts. The cultivation patterns of these crops have increasingly been determined by
# natural rains. With the advent of the drought, Men have opted for Lands which are rich and
# moisture which can sustain the cultivation of the crops. This action has led to increasing
# degrading activities in regions like Burkina Faso, Mali and Gambia. The desire to farm in
# areas closer to water bodies has also led to water pollution. Statistically, poor and erratic
# rainfall in many years
# since 1968 has brought about reduced yields of these crops in the countries and has
# reduced the potential germination of seeds. Particularly the seeds of millet and sorghum
# have suffered a great deal from this instance.
#
# Ghana just like many other tropical countries is very much vulnerable to climate change and
# variability. An estimated 35 percent of the total land mass is desert and since the 1980s the
# has been increasing desertification of the northern part of the country. Desertification in
# Ghana is currently estimated to be proceeding at a rate of 20,000 hectares per annum
# thereby compromising water resource. n northern Ghana, these farmers are usually
# involved in the cultivation of staple grains including maize,
# rice, millet, sorghum, soybean, cowpea and groundnut, and also engage in the rearing
# of small ruminants such as sheep and goat.
# """
#
# uppercase_chars, count = detect_uppercase_chars_excluding_names_locations(text)
#
# print("Uppercase Characters (not at sentence start, excluding names/locations):", uppercase_chars)
# print("Count of Uppercase Characters (not at sentence start, excluding names/locations):", count)

def C3_score(text):
    uppercase_chars, count = detect_uppercase_chars_excluding_names_locations(text)
    if count>0:
        print('------------------- UPPERCASES -------------------')
        print("Uppercases found:")
        print(uppercase_chars)
        return -1
    return 0

# print(C3_score(text))
