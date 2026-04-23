import spacy
import re
import nltk
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required NLTK data if not already available
nltk.download('stopwords')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Load the set of English stopwords from NLTK
stop_words = set(stopwords.words('english'))

# Load a set of common English words from NLTK corpus
english_words = set(words.words())

# Set of common Latin enumerations (Roman numerals)
roman_numerals = {
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"
}

def detect_abbreviations(text):
    # Tokenize the text and tag part-of-speech (POS)
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)

    # Match capitalized words with 2+ letters
    capitalized_words = [word for word, tag in tagged_tokens if word.isupper() and len(word) > 1]

    # Match short forms like Dr., Mr., U.S.A., FBI, PEDs, etc.
    short_forms = re.findall(r'\b([A-Z]{2,}|[A-Z]{1,}[a-z]{1})\b', text)

    abbreviations = []

    # Detect abbreviations from capitalized words
    for word in capitalized_words:
        if word not in roman_numerals and word.lower() not in english_words:
            abbreviations.append(word)

    # Detect abbreviations from short forms
    for short_form in short_forms:
        if short_form.lower() not in english_words and short_form not in roman_numerals:
            abbreviations.append(short_form)

    return abbreviations

def C15_score(text):
    score = 0
    abbreviations = detect_abbreviations(text)

    if abbreviations:
        print("---------------------- ABBREVIATIONS ------------------- ")
        print(f"Abbreviations: {abbreviations}")
        score = -1

    return score

#
# text = """
# Soil erosion is not a general problem in West Africa under indigenous husbandry systems. It
# is, however, locally a chronic problem, and in many areas a potential hazard under changing
# cultivation practices. Soil erosion is intimately associated with problems of water control
# and desertification, and it is thus convenient to consider both together.
#
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
# have suffered a great deal from this instance Alexander II.
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
# print(C15_score(text))
