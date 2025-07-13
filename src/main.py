# Import the C1 to C12 score functions
from C1_spacing_sections import C1_score
from C2_No_I import C2_score
from C3_No_U import C3_score
from C4_Yes_B import C4_score
from C5_no_uppercase import C5_score
from C7_short_sentences import C7_score
from C8_short_paragraphs import C8_score
from C9_sec_headings import C9_score
from C10_toc import C10_score
from C11_active_voice import C11_score
from C12_simple_language import C12_score
from C13_bullet_points import C13_score
from C14_double_negative import C14_score
from C15_no_abbreviations import C15_score
from C17_spacing_headings import C17_score

def main(text):
    # The output is always left aligned so C6 is 1
    C6_score=1

    # The output is always in single column so C16 is 0
    C16_score=0

    # Call each function and get the score (assuming each function returns a numeric value)
    total_score = 0

    # Call each C_score function and sum the results
    C1= C1_score(text)
    C2= C2_score(text)
    C3= C3_score(text)
    C4= C4_score(text)
    C5= C5_score(text)
    C6= C6_score
    C7= C7_score(text)
    C8= C8_score(text)
    C9= C9_score(text)
    C10= C10_score(text)
    C11= C11_score(text)
    C12= C12_score(text)
    C13= C13_score(text)
    C14= C14_score(text)
    C15= C15_score(text)
    C16= C16_score
    C17= C17_score(text)

    #Calculate Visual features
    visual=C1+C2+C3+C4+C5+C6+C9+C10+C13+C16+C17
    # print('visual total score is ', visual, '\n here is each element', C1,C2,C3,C4,C7,C10,C16,C17)

    #Calculate Content features
    content=C7+C8+C11+C12+C14+C15

    print(f"The score for visual features: {visual}")
    print(f"The score for content features: {content}")
    # Print the total score
    print(f"Total Score: {visual+content}")

    return visual,content

if __name__ == "__main__":
    main()
