# Import the C1 to C12 score functions
from C1_spacing_sections import C1_score
from C2_I_U_B import C2_score
from C3_no_uppercase import C3_score
from C5_short_sentences import C5_score
from C6_short_paragraphs import C6_score
from C7_sec_headings_and_toc import C7_score
from C8_active_voice import C8_score
from C9_simple_language import C9_score
from C10_bullet_points import C10_score
from C11_double_negative import C11_score
from C15_no_abbreviations import C15_score
from C17_spacing_headings import C17_score

def main(text):

#     text = """
# As production became mechanized and relocated to factories, the experience of workers underwent significant
# changes. Farmers and artisans had controlled the pace of their labor and the order in which things were done.
# If an artisan wanted to take the afternoon off, he could. If a farmer wished to rebuild his fence on Thursday
# instead of on Wednesday, he could. They conversed and often drank during the workday. Indeed, journeymen
# were often promised alcohol as part of their wages. One member of the group might be asked to read a book or
# a newspaper aloud to the others. In the warm weather, doors and windows might be opened to the outside, and
# work stopped when it was too dark to see.
#
# Work in factories proved to be quite different. Employees were expected to report at a certain time, usually
# early in the morning, and to work all day. They could not leave when they were tired or take breaks other than
# at designated times. Those who arrived late found their pay docked; five minutes’ tardiness could result in
# several hours’ worth of lost pay, and repeated tardiness could result in dismissal. The monotony of repetitive
# tasks made days particularly long. Hours varied according to the factory, but most factory employees toiled ten
# to twelve hours a day, six days a week. In the winter, when the sun set early, oil lamps were used to light the
# factory floor, and employees strained their eyes to see their work and coughed as the rooms filled with smoke
# from the lamps. In the spring, as the days began to grow longer, factories held “blowing-out” celebrations to
# mark the extinguishing of the oil lamps. These “blow-outs” often featured processions and dancing.
#
# Freedom within factories was limited. Drinking was prohibited. Some factories did not allow employees to sit
# down. Doors and windows were kept closed, especially in textile factories where fibers could be easily
# disturbed by incoming breezes, and mills were often unbearably hot and humid in the summer. In the winter,
# workers often shivered in the cold. In such environments, workers’ health suffered.
#
# The workplace posed other dangers as well. The presence of cotton bales alongside the oil used to lubricate
# machines made fire a common problem in textile factories. Workplace injuries were also common. Workers’
# hands and fingers were maimed or severed when they were caught in machines; in some cases, their limbs or
# entire bodies were crushed. Workers who didn’t die from such injuries almost certainly lost their jobs, and
# with them, their income. Corporal punishment of both children and adults was common in factories; where
# abuse was most extreme, children sometimes died as a result of injuries suffered at the hands of an overseer.
#
# As the decades passed, working conditions deteriorated in many mills. Workers were assigned more machines
# to tend, and the owners increased the speed at which the machines operated. Wages were cut in many
# factories, and employees who had once labored for an hourly wage now found themselves reduced to
# piecework, paid for the amount they produced and not for the hours they toiled. Owners also reduced
# compensation for piecework. Low wages combined with regular periods of unemployment to make the lives of
# workers difficult, especially for those with families to support. In New York City in 1850, for example, the
# average male worker earned $300 a year; it cost approximately $600 a year to support a family of five.
#     """


    # The output is always left aligned so C4 is 1
    C4_score=1

    # The output is always in single column so C16 is 0
    C16_score=0

    # Call each function and get the score (assuming each function returns a numeric value)
    total_score = 0

    # Call each C_score function and sum the results
    C1= C1_score(text)
    C2= C2_score(text)
    C3= C3_score(text)
    C4= C4_score
    C5= C5_score(text)
    C6= C6_score(text)
    C7= C7_score(text)
    C8= C8_score(text)
    C9= C9_score(text)
    C10= C10_score(text)
    C11= C11_score(text)
    C15= C15_score(text)
    C16= C16_score
    C17= C17_score(text)

    #Calculate Visual features
    visual=C1+C2+C3+C4+C7+C10+C16+C17
    print('visual total score is ', visual, '\n here is each element', C1,C2,C3,C4,C7,C10,C16,C17)
    # print('C1=',C1)
    # print('C7=',C7)
    #Calculate Content features
    content=C5+C6+C8+C9+C11+C15

    print(f"The score for visual features: {visual}")
    print(f"The score for content features: {content}")
    # Print the total score
    print(f"Total Score: {visual+content}")

    return visual,content

if __name__ == "__main__":
    main()
