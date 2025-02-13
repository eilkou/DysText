# import spacy
# import re
# import nltk
# from nltk.corpus import words, stopwords
# from nltk.probability import FreqDist
# from geopy.geocoders import Nominatim
#
# # Download required NLTK data if not already available
# nltk.download('stopwords')
# nltk.download('words')
# nltk.download('punkt')
#
# # Load the spaCy English model
# nlp = spacy.load('en_core_web_sm')
#
# # Load the set of English stopwords from NLTK and spaCy
# stop_words = set(stopwords.words('english'))
#
# # Load a set of common English words from NLTK corpus
# english_words = set(words.words())
#
# # Initialize geolocator
# geolocator = Nominatim(user_agent="geolocator")
#
#
# # C12a: No jargon's nor abbreviations - jargons
# def detect_jargon(text):
#     """
#     Detects jargon in a given text based on the rarity of the words compared to a general English corpus,
#     excluding stopwords, punctuation, numbers, past-tense verbs, plural nouns, and country/continent names.
#
#     Args:
#     text (str): The input text to analyze.
#
#     Returns:
#     list: A list of words that are likely jargon.
#     """
#
#
#     # List of countries and continents to exclude (you can extend this list as needed)
#     countries_and_continents = set([
#         "afghanistan", "albania", "algeria", "andorra", "angola", "antigua", "argentina", "armenia", "australia", "austria",
#         "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan",
#         "bolivia", "bosnia", "botswana", "brazil", "brunei", "bulgaria", "burkina", "burundi", "cabo verde", "cambodia",
#         "cameroon", "canada", "central african republic", "chad", "chile", "china", "colombia", "comoros", "congo", "congo (democratic republic)",
#         "costa rica", "croatia", "cuba", "cyprus", "czech republic", "denmark", "djibouti", "dominica", "dominican republic", "ecuador",
#         "egypt", "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france",
#         "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guinea-bissau", "guyana",
#         "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "jamaica",
#         "japan", "jordan", "kazakhstan", "kenya", "kiribati", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon",
#         "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "madagascar", "malawi", "malaysia", "maldives",
#         "mali", "malta", "marshall islands", "mauritania", "mauritius", "mexico", "micronesia", "moldova", "monaco", "mongolia",
#         "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands", "new zealand", "nicaragua",
#         "niger", "nigeria", "north korea", "north macedonia", "norway", "oman", "pakistan", "palau", "panama", "papua new guinea",
#         "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis",
#         "saint lucia", "saint vincent and the grenadines", "samoa", "san marino", "sao tome and principe", "saudi arabia", "senegal",
#         "serbia", "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon islands", "somalia", "south africa",
#         "south korea", "south sudan", "spain", "sri lanka", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan",
#         "tanzania", "thailand", "timor-leste", "togo", "tonga", "trinidad and tobago", "tunisia", "turkmenistan", "turkey", "tuvalu",
#         "uganda", "ukraine", "united arab emirates", "united kingdom", "united states", "uruguay", "uzbekistan", "vanuatu", "vatican city",
#         "venezuela", "vietnam", "yemen", "zambia", "zimbabwe", "africa", "asia", "europe", "oceania", "north america", "south america"
#     ])
#
#
#     # List of nationalities and ethnic group terms to exclude (you can extend this list as needed)
#     nationalities_and_ethnic_groups = set([
#         # Nationalities
#         "afghan", "albanian", "algerian", "andorran", "angolan", "antiguans", "argentine", "armenian", "australian", "austrian",
#         "azerbaijani", "bahamian", "bahraini", "bangladeshi", "barbadian", "belarusian", "belgian", "belizean", "beninese", "bhutani",
#         "bolivian", "bosnian", "botswanan", "brazilian", "british", "bruneian", "bulgarian", "burkinabé", "burundian", "cabo verdean", "cambodian",
#         "cameroonian", "canadian", "central african", "chadian", "chilean", "chinese", "colombian", "comorian", "congolese", "costa rican",
#         "croatian", "cuban", "cypriot", "czech", "danish", "djiboutian", "dominican", "dominican republic", "ecuadorian", "egyptian",
#         "el salvadoran", "equatorial guinean", "eritrean", "estonian", "eswatini", "ethiopian", "fijian", "finnish", "french",
#         "gabonese", "gambian", "georgian", "german", "ghanian", "greek", "grenadian", "guatemalan", "guinean", "guinea-bissauan", "guyanese",
#         "haitian", "honduran", "hungarian", "icelandic", "indian", "indonesian", "iranian", "iraqi", "irish", "israeli", "italian", "jamaican",
#         "japanese", "jordanian", "kazakh", "kenyan", "kiribatian", "kosovar", "kuwaiti", "kyrgyzstani", "laotian", "latvian", "lebanese",
#         "lesotho", "liberian", "libyan", "liechtensteinian", "lithuanian", "luxembourger", "madagascan", "malawian", "malaysian", "maldivian",
#         "malian", "maltese", "marshallese", "mauritanian", "mauritian", "mexican", "micronesian", "moldovan", "monacan", "mongolian",
#         "montenegrin", "moroccan", "mozambican", "myanmarese", "namibian", "nauruan", "nepalese", "netherlandish", "new zealander", "nicaraguan",
#         "nigerian", "nigerien", "north korean", "north macedonian", "norwegian", "omani", "pakistani", "palauan", "panamanian", "papua new guinean",
#         "paraguayan", "peruvian", "philippine", "polish", "portuguese", "qatari", "romanian", "russian", "rwandan", "saint kitts and nevisian",
#         "saint lucian", "saint vincentian", "samoan", "san marinian", "sao tomean", "saudi", "senegalese", "serbian", "seychellois", "sierra leonean",
#         "singaporean", "slovak", "slovene", "solomon islander", "somali", "south african", "south korean", "south sudanese", "spanish", "sri lankan",
#         "sudanese", "surinamese", "swedish", "swiss", "syrian", "taiwanese", "tajik", "tanzanian", "thai", "timorese", "togolese", "tongan",
#         "trinidadian", "tunisian", "turkmen", "turkish", "tuvaluan", "ugandan", "ukrainian", "united arab emirate", "united kingdom", "united states",
#         "uruguayan", "uzbek", "vanuatuan", "vatican city", "venezuelan", "vietnamese", "yemeni", "zambian", "zimbabwean",
#
#         # Ethnic Groups
#         "african", "asian", "european", "north american", "south american", "oceanian", "arab", "black", "caucasian", "hispanic", "latino",
#         "native american", "pacific islander", "romani", "gypsy", "aboriginal", "maori", "sami", "pict", "tamil", "hindu", "sikh", "kurdish",
#         "berber", "romani", "gypsy", "sinti", "chicano", "celtic", "baltic", "slavic", "romance", "germanic", "indo-european", "tibetan", "mongoloid",
#         "austronesian", "dravidian", "jewish", "armenian", "basque", "somali", "georgian", "berber", "mestizo", "mulatto", "creole", "zulu", "xhosa",
#
#         # Continental terms
#         "asian", "african", "european", "north american", "south american", "oceanian", "middle eastern", "latin american", "caribbean", "pacific islander",
#         "sub-saharan", "scandinavian", "latin", "oriental", "asian-pacific", "indian ocean", "eastern european", "western european", "southern european",
#         "nordic", "caucasus", "central asian", "east asian", "south asian", "south pacific"
#     ])
#
#
#     # Remove newlines before processing
#     text = text.replace("\n", " ")
#
#     # Process the text using spaCy for POS tagging and other annotations
#     doc = nlp(text)
#
#     jargon = []
#
#     # Frequency distribution of words in a general English corpus (nltk words)
#     freq_dist = FreqDist(english_words)
#
#     # Tokenize and process the text
#     for token in doc:
#         # Exclude stopwords, punctuation, numbers, and plural nouns
#         if not token.is_stop and not token.is_punct and not token.like_num:
#             word = token.text.lower()
#
#             # Exclude past-tense verbs (VBD, VBN) using POS tagging
#             if token.pos_ == "VERB" and token.tag_ in ["VBD", "VBN"]:
#                 continue
#
#             # Exclude continuous (progressive) verbs (VBG)
#             if token.pos_ == "VERB" and token.tag_ == "VBG":
#                 continue
#
#             # Exclude plural nouns (NNS, NNPS)
#             if token.pos_ == "NOUN" and token.tag_ in ["NNS", "NNPS"]:
#                 continue
#
#             # Exclude country/continent names
#             if word in countries_and_continents:
#                 continue
#
#             # Exclude nationalities and ethnic group terms
#             if word in nationalities_and_ethnic_groups:
#                 continue
#
#             # Check if the word is a plural form of a nationality or ethnicity term
#             if word.endswith("s") and word[:-1] in nationalities_and_ethnic_groups:
#                 continue
#
#             # Check if the word is uncommon and not a general English word
#             if word not in english_words:
#                 jargon.append(word)
#
#     # Now check if any of the jargon words are cities, and filter them out
#     jargon = [word for word in jargon if not is_city(word)]
#
#     return list(set(jargon))  # Return only unique jargon words
#
#
# def is_city(word):
#     """
#     Check if a word corresponds to a valid city using Geopy's Nominatim geocoding service.
#
#     Args:
#     word (str): The word to check if it corresponds to a city.
#
#     Returns:
#     bool: True if the word is a city, False otherwise.
#     """
#     location = geolocator.geocode(word, language='en', exactly_one=True)
#     if location:
#         return True
#     return False
#
# # C12b: No jargon's nor abbreviations - abbreviations
# def detect_abbreviations(text):
#     # Match abbreviations like NASA, AI, or Dr.
#     abbreviations = re.findall(r'\b[A-Z]{2,}\b', text)  # Capitalized words with 2+ letters
#     short_forms = re.findall(r'\b[A-Za-z]\.\b', text)   # Short forms like Dr., e.g.
#     return abbreviations + short_forms


# text = "We need to integrate blockchain and neural networks into our AI-powered systems."
#
# abbreviations=detect_abbreviations(text)
# print(f"Has abbreviations: ", len(abbreviations)>0)
# print(f"Abbreviations: ", abbreviations)
#
# detected_jargon = detect_jargon(text)
# print("Has Jargon:", len(detected_jargon)>0)
# print("Detected Jargon:", detected_jargon)
#
# def C12_score(text):
#     score=0
#     abbreviations=detect_abbreviations(text)
#     detected_jargon = detect_jargon(text)
#     if len(abbreviations)>0:
#         print(f"Abbreviations: ", abbreviations)
#         score=-1
#     if len(detected_jargon)>0:
#         print("Detected Jargon:", detected_jargon)
#         score=-1
#     return score

# print(C12_score(text))

#
# import spacy
# import re
# import nltk
# from nltk.corpus import words, stopwords
# from nltk.probability import FreqDist
# from geopy.geocoders import Nominatim
#
# # Download required NLTK data if not already available
# nltk.download('stopwords')
# nltk.download('words')
# nltk.download('punkt')
#
# # Load the spaCy English model
# nlp = spacy.load('en_core_web_sm')
#
# # Load the set of English stopwords from NLTK and spaCy
# stop_words = set(stopwords.words('english'))
#
# # Load a set of common English words from NLTK corpus
# english_words = set(words.words())
#
# # Initialize geolocator
# geolocator = Nominatim(user_agent="geolocator")
#
#
# # C12a: No jargon's nor abbreviations - jargons
# def detect_jargon(text):
#     """
#     Detects jargon in a given text based on the rarity of the words compared to a general English corpus,
#     excluding stopwords, punctuation, numbers, past-tense verbs, plural nouns, and location names (using NER).
#
#     Args:
#     text (str): The input text to analyze.
#
#     Returns:
#     list: A list of words that are likely jargon.
#     """
#
#     # Remove newlines before processing
#     text = text.replace("\n", " ")
#
#     # Process the text using spaCy for POS tagging and other annotations
#     doc = nlp(text)
#
#     jargon = []
#
#     # Frequency distribution of words in a general English corpus (nltk words)
#     freq_dist = FreqDist(english_words)
#
#     # Extract locations from NER entities
#     locations = set()
#     for ent in doc.ents:
#         if ent.label_ in ["GPE", "LOC"]:  # GPE = Geopolitical Entity (e.g., country, city, etc.), LOC = Location
#             locations.add(ent.text.lower())
#
#     # Tokenize and process the text
#     for token in doc:
#         # Exclude stopwords, punctuation, numbers, and plural nouns
#         if not token.is_stop and not token.is_punct and not token.like_num:
#             word = token.text.lower()
#
#             # Exclude past-tense verbs (VBD, VBN) using POS tagging
#             if token.pos_ == "VERB" and token.tag_ in ["VBD", "VBN"]:
#                 continue
#
#             # Exclude continuous (progressive) verbs (VBG)
#             if token.pos_ == "VERB" and token.tag_ == "VBG":
#                 continue
#
#             # Exclude plural nouns (NNS, NNPS)
#             if token.pos_ == "NOUN" and token.tag_ in ["NNS", "NNPS"]:
#                 continue
#
#             # Exclude location names identified by NER
#             if word in locations:
#                 continue
#
#             # Check if the word is uncommon and not a general English word
#             if word not in english_words:
#                 jargon.append(word)
#
#     return list(set(jargon))  # Return only unique jargon words


import spacy
import re
import nltk
from nltk.corpus import words, stopwords
from nltk.probability import FreqDist
from geopy.geocoders import Nominatim
from nltk import pos_tag, word_tokenize

# Download required NLTK data if not already available
nltk.download('stopwords')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Load the set of English stopwords from NLTK and spaCy
stop_words = set(stopwords.words('english'))

# Load a set of common English words from NLTK corpus
english_words = set(words.words())

# Initialize geolocator
geolocator = Nominatim(user_agent="geolocator")

# Example: Add a set of domain-specific jargon (for demonstration, could be technical terms, industry-specific, etc.)
domain_jargon = set([
    'blockchain', 'ai', 'cloud', 'docker', 'kubernetes', 'bigdata', 'cybersecurity', 'machinelearning', 'AD',
])

# Extend to include common abbreviations/acronyms
acronyms = set([
    'API', 'URL', 'HTTP', 'JSON', 'RAM', 'CPU', 'IP', 'TCP', 'SQL', 'SEO'
])

not_jargon= set([
    'archeological', 'etc', 'expertise', 'favourable', 'socio', 'advent', 'faso', 'states', 'burkina', 'annum', 'leone', 'savannah', 'meccans', 'upgrading', 'having', 'english', 'trans', 'fortified', 'enslaved', 'tangier', 'meantime', 'centre', 'coastline', 'islands', 'gwatón', 'pre', 'regions', 'servicemen', 'coordinating', 'disgruntled', 'paved', 'campaigning', 'wider', 'newfound', 'defining', 'armour', 'remembering', 'buying', 'frying', 'rocks', 'famed', 'moses','i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx', 'esteemed', 'upbringing'
])

# List of month names (both capitalized and lowercase)
months = set([
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
    'september', 'october', 'november', 'december'
])

# List of countries and continents to exclude (you can extend this list as needed)
countries_and_continents = set([
    "afghanistan", "albania", "algeria", "andorra", "angola", "antigua", "argentina", "armenia", "australia", "austria",
    "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan",
    "bolivia", "bosnia", "botswana", "brazil", "brunei", "bulgaria", "burkina", "burundi", "cabo verde", "cambodia",
    "cameroon", "canada", "central african republic", "chad", "chile", "china", "colombia", "comoros", "congo", "congo (democratic republic)",
    "costa rica", "croatia", "cuba", "cyprus", "czech republic", "denmark", "djibouti", "dominica", "dominican republic", "ecuador",
    "egypt", "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france",
    "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guinea-bissau", "guyana",
    "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "jamaica",
    "japan", "jordan", "kazakhstan", "kenya", "kiribati", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon",
    "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "madagascar", "malawi", "malaysia", "maldives",
    "mali", "malta", "marshall islands", "mauritania", "mauritius", "mexico", "micronesia", "moldova", "monaco", "mongolia",
    "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands", "new zealand", "nicaragua",
    "niger", "nigeria", "north korea", "north macedonia", "norway", "oman", "pakistan", "palau", "panama", "papua new guinea",
    "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis",
    "saint lucia", "saint vincent and the grenadines", "samoa", "san marino", "sao tome and principe", "saudi arabia", "senegal",
    "serbia", "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon islands", "somalia", "south africa",
    "south korea", "south sudan", "spain", "sri lanka", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan",
    "tanzania", "thailand", "timor-leste", "togo", "tonga", "trinidad and tobago", "tunisia", "turkmenistan", "turkey", "tuvalu",
    "uganda", "ukraine", "united arab emirates", "united kingdom", "united states", "uruguay", "uzbekistan", "vanuatu", "vatican city",
    "venezuela", "vietnam", "yemen", "zambia", "zimbabwe", "africa", "asia", "europe", "oceania", "north america", "south america", "sahara", "constantinople", "são", "bugendo", "sebastião", "domingos", "santa", "kwamena", "tomé", "verde", "coquard", "slessor", "del", "vatican", "st.", "della"
])

names = set([
    "francis", "lisa", "leonardo", "verrocchio", "stephen", "andrea", "marie", "mohammed", "khaled", "joao", "jerome", "alessandro", "filipepi", "catherine", "ciarla"
])

# List of nationalities and ethnic group terms to exclude (you can extend this list as needed)
nationalities_and_ethnic_groups = set([
    # Nationalities
    "afghan", "albanian", "algerian", "andorran", "angolan", "antiguans", "argentine", "armenian", "australian", "austrian",
    "azerbaijani", "bahamian", "bahraini", "bangladeshi", "barbadian", "belarusian", "belgian", "belizean", "beninese", "bhutani",
    "bolivian", "bosnian", "botswanan", "brazilian", "british", "bruneian", "bulgarian", "burkinabé", "burundian", "cabo verdean", "cambodian",
    "cameroonian", "canadian", "central african", "chadian", "chilean", "chinese", "colombian", "comorian", "congolese", "costa rican",
    "croatian", "cuban", "cypriot", "czech", "danish", "djiboutian", "dominican", "dominican republic", "ecuadorian", "egyptian",
    "el salvadoran", "equatorial guinean", "eritrean", "estonian", "eswatini", "ethiopian", "fijian", "finnish", "french",
    "gabonese", "gambian", "georgian", "german", "ghanian", "greek", "grenadian", "guatemalan", "guinean", "guinea-bissauan", "guyanese",
    "haitian", "honduran", "hungarian", "icelandic", "indian", "indonesian", "iranian", "iraqi", "irish", "israeli", "italian", "jamaican",
    "japanese", "jordanian", "kazakh", "kenyan", "kiribatian", "kosovar", "kuwaiti", "kyrgyzstani", "laotian", "latvian", "lebanese",
    "lesotho", "liberian", "libyan", "liechtensteinian", "lithuanian", "luxembourger", "madagascan", "malawian", "malaysian", "maldivian",
    "malian", "maltese", "marshallese", "mauritanian", "mauritian", "mexican", "micronesian", "moldovan", "monacan", "mongolian",
    "montenegrin", "moroccan", "mozambican", "myanmarese", "namibian", "nauruan", "nepalese", "netherlandish", "new zealander", "nicaraguan",
    "nigerian", "nigerien", "north korean", "north macedonian", "norwegian", "omani", "pakistani", "palauan", "panamanian", "papua new guinean",
    "paraguayan", "peruvian", "philippine", "polish", "portuguese", "qatari", "romanian", "russian", "rwandan", "saint kitts and nevisian",
    "saint lucian", "saint vincentian", "samoan", "san marinian", "sao tomean", "saudi", "senegalese", "serbian", "seychellois", "sierra leonean",
    "singaporean", "slovak", "slovene", "solomon islander", "somali", "south african", "south korean", "south sudanese", "spanish", "sri lankan",
    "sudanese", "surinamese", "swedish", "swiss", "syrian", "taiwanese", "tajik", "tanzanian", "thai", "timorese", "togolese", "tongan",
    "trinidadian", "tunisian", "turkmen", "turkish", "tuvaluan", "ugandan", "ukrainian", "united arab emirate", "united kingdom", "united states",
    "uruguayan", "uzbek", "vanuatuan", "vatican city", "venezuelan", "vietnamese", "yemeni", "zambian", "zimbabwean", "scottish", "sisters", "roman", "europeans", "ethiopians",

    # Ethnic Groups
    "african", "asian", "european", "north american", "south american", "oceanian", "arab", "black", "caucasian", "hispanic", "latino",
    "native american", "pacific islander", "romani", "gypsy", "aboriginal", "maori", "sami", "pict", "tamil", "hindu", "sikh", "kurdish",
    "berber", "romani", "gypsy", "sinti", "chicano", "celtic", "baltic", "slavic", "romance", "germanic", "indo-european", "tibetan", "mongoloid",
    "austronesian", "dravidian", "jewish", "armenian", "basque", "somali", "georgian", "berber", "mestizo", "mulatto", "creole", "zulu", "xhosa", "islamic", "momodou","islam", "christian", "ottoman","arabic", "christianity","presbyterians", "catholics","methodists",

    # Continental terms
    "asian", "african", "european", "north american", "south american", "oceanian", "middle eastern", "latin american", "caribbean", "pacific islander",
    "sub-saharan", "scandinavian", "latin", "oriental", "asian-pacific", "indian ocean", "eastern european", "western european", "southern european",
    "nordic", "caucasus", "central asian", "east asian", "south asian", "south pacific", "saharan"
])

def detect_jargon(text):
    """
    Detects jargon in a given text based on the rarity of the words compared to a general English corpus,
    excluding stopwords, punctuation, numbers, past-tense verbs, plural nouns, and location names (using NER).
    Includes detection for domain-specific jargon and common abbreviations.

    Args:
    text (str): The input text to analyze.

    Returns:
    list: A list of words that are likely jargon.
    """

    # Remove newlines before processing
    text = text.replace("\n", " ")

    # Process the text using spaCy for POS tagging and other annotations
    doc = nlp(text)

    jargon = []

    # Frequency distribution of words in a general English corpus (nltk words)
    freq_dist = FreqDist(english_words)

    # Extract locations from NER entities
    locations = set()
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:  # GPE = Geopolitical Entity (e.g., country, city, etc.), LOC = Location
            locations.add(ent.text.lower())
        if ent.label_ in ["PERSON"]:
            names.add(ent.text.lower())

    # Tokenize and process the text
    for token in doc:
        # Exclude stopwords, punctuation, numbers, and plural nouns
        if not token.is_stop and not token.is_punct and not token.like_num:
            word = token.text.lower()

            # Make sure we don't add empty strings
            if word == ' ' or word == '     ' or word == '    ' or word == '   ' or word == '  ':  # Check for empty or whitespace-only strings
                continue

            # Exclude nationalities and ethnicities and countries
            if word in nationalities_and_ethnic_groups or word in countries_and_continents:
                continue

            # Exclude months
            if word in months:
                continue

            # Exclude names
            if word in names:
                continue


            # Exclude comparative and superlative adjectives (e.g., greater, greatest)
            if token.tag_ == "JJR" or token.tag_ == "JJS":  # JJR = Comparative Adjective, JJS = Superlative Adjective
                continue

            # Exclude past-tense verbs (VBD, VBN) using POS tagging
            if token.pos_ == "VERB" and token.tag_ in ["VBD", "VBN", "VBG"]:
                continue

            # Exclude continuous (progressive) verbs (VBG)
            if token.pos_ == "VERB" and token.tag_ == "VBG":
                continue

            # Exclude all conjugated verbs and their forms
            if token.pos_ == "VERB" and token.lemma_ != word:  # If the lemma is different, it's conjugated
                continue  # Skip conjugated verbs like "uses"

            # Exclude plural nouns (NNS, NNPS)
            if token.pos_ == "NOUN" and token.tag_ in ["NNS", "NNPS"]:
                continue

            # Exclude location names identified by NER
            if word in locations:
                continue

             # Excludealphabetic enumerations
            if len(word) == 1 and word.isalpha():
                continue

            # Exclude unusual words captured as jargon when they shouldn't
            if word in not_jargon:
                continue

            # Check if the word is uncommon and not a general English word
            if word not in english_words and word not in domain_jargon and word not in acronyms:
                jargon.append(word)

    # Return only unique jargon words
    return list(set(jargon))




def detect_abbreviations(text):
    # # Match abbreviations like NASA, AI, or Dr.
    # capitalized_words = re.findall(r'\b[A-Z]{2,}\b', text)  # Capitalized words with 2+ letters
    # short_forms = re.findall(r'\b[A-Za-z]\.\b', text)   # Short forms like Dr., e.g.
    #
    # # Filter out capitalized words that are valid English words
    # abbreviations = []
    # for word in capitalized_words:
    #     # If the word is not in the dictionary and is a valid abbreviation (e.g., all caps but not in dictionary)
    #     if word.lower() not in english_words and not word.islower():
    #         abbreviations.append(word)
    #
    # return abbreviations + short_forms

    # Tokenize the text and tag part-of-speech (POS)
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)

    # Match capitalized words with 2+ letters
    capitalized_words = [word for word, tag in tagged_tokens if word.isupper() and len(word) > 1]

    # Match short forms like Dr., Mr., U.S.A., FBI, PEDs, etc.
    short_forms = re.findall(r'\b([A-Z]{2,}|[A-Z]{1,}[a-z]{1})\b', text)

    # Set of common Latin enumerations (Roman numerals)
    roman_numerals = {
        "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
        "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
        "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"
    }

    abbreviations = []

    for word in capitalized_words:
        # Check if the word is in the dictionary
        if word.lower() not in english_words:
            # Check if the word is a proper noun (using POS tagging)
            if word not in english_words and not any(tag.startswith('NNP') for word, tag in tagged_tokens if word == word):
                abbreviations.append(word)

    # Filter detected abbreviations to exclude common words
    for short_form in short_forms:
        # Exclude if it's a common word in English (like "In", "To", "By") or a Latin enumeration
        if short_form.lower() not in english_words and short_form not in roman_numerals:
            abbreviations.append(short_form)

    return abbreviations

def C12_score(text):
    score = 0
    abbreviations = detect_abbreviations(text)
    detected_jargon = detect_jargon(text)

    if len(abbreviations) > 0:
        print("---------------------- ABBREVIATIONS ------------------- ")
        print(f"Abbreviations: ", abbreviations)
        score = score-1

    if len(detected_jargon) > 0:
        print("---------------------- JARGONS ------------------- ")
        print("Detected Jargons:", detected_jargon)
        score =score -1

    return score

