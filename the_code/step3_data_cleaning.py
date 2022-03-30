import pandas as pd
import numpy as np 


# Dataframe 

df1 = pd.read_csv('source/merge/data-merge2.csv', low_memory=False)

# Variables from the public teacher file: S4A
# - Age
# - Sex
# - Race and Ethnicity
# - Total Teaching Experience
# - Main Teaching Assignment
# - One more variable of your team's choice
left_teaching = df1[(df1['STATUS']=='L')]
age = df1['AGE_T']
gender = df1['T0356'] #1 Male #2 Female
race = df1['RACETH_T'] # Look at code book.
teaching_experiance = df1['TOTEXPER'] # The code for t3 and t2
main_teaching_assignment = df1['ASSIGN'] # Universal main teaching assignment 
mentorteach_help = df1['T0149'] # extent that mentor helped 

#STATUS = Q: Final Teacher Status: Indicates whether the respondent is a M, S, or L
#STATUS = A: M = "Mover", S = "Stayer", L = "Leaver"
def stopteach():
    movers = df1[ (df1['STATUS']=='M')  ]
    total_movers = movers.shape[0]
    stayers = df1[  (df1['STATUS']=='S')  ]
    total_stayers = stayers.shape[0]
    leavers = df1[  (df1['STATUS']=='L')  ]
    total_leavers = leavers.shape[0]

    sum_of_respondants_to_stopteach = np.sum(total_movers + total_stayers + total_leavers)
    summary_of_respondants_to_stopteach = df1[ "STATUS" ].describe()

    print("Final Teacher Status:")
    print(f'the total number of teachers that moved to another school: {total_movers}')
    print(f'the total number of teachers that stayed at the same school: {total_stayers}')
    print(f'the total number of teachers that left teaching: {total_leavers}')
    print(f'To verify the sum of responses to "status": {sum_of_respondants_to_stopteach}')
    print(summary_of_respondants_to_stopteach)
    print()

#AGE_T = Q: Age of the Teacher.
#AGE_T = A: 1 = "Less than 30 years", 2 = "30 to 39 years", 3 = "40 to 49 years", 4 = "50 years or older"
def teachage():
    less_than_XXX = df1[ (df1['AGE_T']==1)  ]
    total_less_than_XXX = less_than_XXX.shape[0]
    XXX_to_XXXIX = df1[  (df1['AGE_T']==2)  ]
    total_XXX_to_XXXIX = XXX_to_XXXIX.shape[0]
    XXXX_to_XLIX = df1[  (df1['AGE_T']==3)  ]
    total_XXXX_to_XLIX = XXXX_to_XLIX.shape[0]
    older_than_L = df1[  (df1[ 'AGE_T']==4)  ]
    total_older_than_L = older_than_L.shape[0]

    sum_of_respondants_to_teachage = np.sum(total_less_than_XXX + total_XXX_to_XXXIX + total_XXXX_to_XLIX + total_older_than_L)
    summary_of_respondants_to_teachage = df1[ "AGE_T" ].describe()

    print("Teachers categorized by age group:")
    print(f'the total number of teachers that are less than 30 years: {total_less_than_XXX}')
    print(f'the total number of teachers that are 30 to 39 years: {total_XXX_to_XXXIX}')
    print(f'the total number of teachers that are 40 to 49 years: {total_XXXX_to_XLIX}')
    print(f'the total number of teachers that are 50 years or older: {total_older_than_L}')
    print(f'To verify the sum of responses to "teacher age": {sum_of_respondants_to_teachage}')
    print(summary_of_respondants_to_teachage)
    print()

#T0356 = Q: Are you male or female?
#T0356 = A: 2 = "Female", 1 = "Male"
def sex():
    male = df1[ (df1['T0356']==1)  ]
    total_male = male.shape[0]
    female = df1[  (df1['T0356']==2)  ]
    total_female = female.shape[0]

    sum_of_respondants_to_sex = np.sum(total_male + total_female)
    summary_of_respondants_to_sex = df1[ "T0356" ].describe()

    print("How many teachers are male and female?")
    print(f'the total number of teachers that are male: {total_male}')
    print(f'the total number of teachers that are female: {total_female}')
    print(f'To verify the sum of responses to "teacher age": {sum_of_respondants_to_sex}')
    print(f'The proportion of ')
    print(summary_of_respondants_to_sex)
    print()

#RACETH_T = Q: Race and Ethnicity.
#RACETH_T = A: 1 = "American Indian", 2 = "Asian", 3 = "Black", 4 = "White", 5 = "Hispanic"
def raza():
    native = df1[ (df1['RACETH_T']==1)  ]
    total_native = native.shape[0]
    asian = df1[  (df1['RACETH_T']==2)  ]
    total_asian = asian.shape[0]
    black = df1[  (df1['RACETH_T']==3)  ]
    total_black = black.shape[0]
    white = df1[  (df1[ 'RACETH_T']==4)  ]
    total_white = white.shape[0]
    hispanic = df1[  (df1[ 'RACETH_T']==5)  ]
    total_hispanic = hispanic.shape[0]

    sum_of_respondants_to_raza = np.sum(total_native + total_asian + total_black + total_white + total_hispanic)
    summary_of_respondants_to_raza = df1[ "RACETH_T" ].describe()

    print("What color are you?")
    print(f'the total number of teachers that are American Indian or Alaska Native, non-Hispanic: {total_native}')
    print(f'the total number of teachers that are Asian or Pacific Islander, non-Hispanic: {total_asian}')
    print(f'the total number of teachers that are Black, non-Hispanic: {total_black}')
    print(f'the total number of teachers that are White, non-Hispanic: {total_white}')
    print(f'the total number of teachers that are Hispanic, regardless of race: {total_hispanic}')
    print(f'To verify the sum of responses to "teacher age": {sum_of_respondants_to_raza}')
    print(summary_of_respondants_to_raza)
    print()

#TOTEXPER = Q: Total teaching experience at time of TFS
#TOTEXPER = A: 1 = "Teacher has taught 3 years or less", 2 = "Teacher has taught more than 3 years"
def teachex():
    # threeless = df1[ (df1['TOTEXPER']==1)  ]
    # total_threeless = threeless.shape[0]
    # threemore = df1[  (df1['TOTEXPER']==2)  ]
    # total_threemore = threemore.shape[0]

    # sum_of_respondants_to_teachex = np.sum(total_threeless + total_threemore)
    summary_of_respondants_to_teachex = df1[ "TOTEXPER" ].describe()

    print("Teacher's total number of years teaching full or part-time in public and private schools?")
    # print(f'the total number of teachers that have taught 3 years or less: {total_threeless}')
    # print(f'the total number of teachers that have taught more than 3 years: {total_threemore}')
    # print(f'To verify the sum of responses to "teacher experience: {sum_of_respondants_to_teachex}')
    print(summary_of_respondants_to_teachex)
    print()

#ASSIGN = Q: General field of SASS main assignment.
#ASSIGN = A: 1 = "Prekindergarten, kindergarten, and generla elementary", 2 = "Math and science", 3 = "English/language arts", 4 = "Social science", 5 = "Special education", 6 = "Foreign languages", 7 = "Bilingual/ESL education", 8 = "Vocational/technical education", 9 = "All others"
def mainass():
    prek = df1[ (df1['ASSIGN']==1)  ]
    total_prek = prek.shape[0]
    stem = df1[  (df1['ASSIGN']==2)  ]
    total_stem = stem.shape[0]
    english = df1[  (df1['ASSIGN']==3)  ]
    total_english = english.shape[0]
    socialsci = df1[  (df1[ 'ASSIGN']==4)  ]
    total_socialsci = socialsci.shape[0]
    speed = df1[  (df1[ 'ASSIGN']==5)  ]
    total_speed = speed.shape[0]
    foreign = df1[  (df1[ 'ASSIGN']==6)  ]
    total_foreign = foreign.shape[0]
    bilingual = df1[  (df1[ 'ASSIGN']==7)  ]
    total_bilingual = bilingual.shape[0]
    technical = df1[  (df1[ 'ASSIGN']==8)  ]
    total_technical = technical.shape[0]
    allother = df1[  (df1[ 'ASSIGN']==9)  ]
    total_allother = allother.shape[0]

    sum_of_respondants_to_mainass = np.sum(total_prek + total_stem + total_english + total_socialsci + total_speed + total_foreign + total_bilingual + total_technical + total_allother)
    summary_of_respondants_to_mainass = df1[ "ASSIGN" ].describe()

    print("What is the teachers general field/main assignment?")
    it = "The total number of teachers that teach"
    print(f'{it} Prekindergarten, kindergarten, and generla elementary: {total_prek}')
    print(f'{it} Math and science: {total_stem}')
    print(f'{it} English/language arts: {total_english}')
    print(f'{it} Social science: {total_socialsci}')
    print(f'{it} Special education: {total_speed}')
    print(f'{it} Foreign languages: {total_foreign}')
    print(f'{it} Bilingual/ESL education: {total_bilingual}')
    print(f'{it} Vocational/technical education: {total_technical}')
    print(f'{it} all other: {total_allother}')
    print(f'To verify the sum of responses to "teacher experience: {sum_of_respondants_to_mainass}')
    print(summary_of_respondants_to_mainass)
    print()

#T0149 = Q: In your first year of teaching, to what extent did your master or mentor teacher help you?
#T0149 = A: 1 = Not at all, 2 = To little extent, 3 = To some extent, 4 = To a good extent, 5 = To a great extent 
def padawan():
    nope = df1[ (df1['T0149']==1)  ]
    total_nope = nope.shape[0]
    little = df1[  (df1['T0149']==2)  ]
    total_little = little.shape[0]
    some = df1[  (df1['T0149']==3)  ]
    total_some = some.shape[0]
    good = df1[  (df1['T0149']==4)  ]
    total_good = good.shape[0]
    great = df1[  (df1['T0149']==5)  ]
    total_great = great.shape[0]

    sum_of_respondants_to_padawan = np.sum(total_nope + total_little + total_some + total_good + total_great)
    summary_of_respondants_to_padawan = df1[ "T0149" ].describe()

    print("In your first year of teaching, to what extent did your master or mentor teacher help you?")
    print(f'The number of teachers that responded with "Not at all": {total_nope}')
    print(f'The number of teachers that responded with "To little extent": {total_little}')
    print(f'The number of teachers that responded with "To some extent": {total_some}')
    print(f'The number of teachers that responded with "To a good extent": {total_good}')
    print(f'The number of teachers that responded with "To a great extent": {total_great}')
    print(f'To verify the sum of responses to "teacher experience: {sum_of_respondants_to_padawan}')
    print(summary_of_respondants_to_padawan)
    print()

#Variables from the public-school file: S3A
# - percent of minority student enrollment share;
# - school levels 3 categories
# - one more variable of your team’s choice;
enrollment_share = df1['S0101'] # total enrollment by race and ethnicity??
school_level = df1['SCHLEVEL_y'] #Team choice one or more variables from public school file
school_level = df1['ATTACK'] #Student attack, ever, past 12 mos

#S0101 = Q: Total enrollment
#S0101 = A: 1 = "Fewer than 300", 2 = "300 - 499", 3 = "500 or more"
def enroll():
    few_CCC = df1[ (df1['S0101']==1)  ]
    total_few_CCC = few_CCC.shape[0]
    CCC_to_CDXCIX = df1[  (df1['S0101']==2)  ]
    total_CCC_to_CDXCIX = CCC_to_CDXCIX.shape[0]
    D_more = df1[  (df1['S0101']==3)  ]
    total_D_more = D_more.shape[0]

    sum_of_respondants_to_enroll = np.sum(total_few_CCC + total_CCC_to_CDXCIX + total_D_more)
    summary_of_respondants_to_enroll = df1[ "S0101" ].describe()

    print("How many students are enolled?")
    it = "There are"
    print(f'{it} {total_few_CCC} schools with fewer than 300 students.')
    print(f'{it} {total_CCC_to_CDXCIX} schools with between 300 and 499 students.')
    print(f'{it} {total_D_more} schools with more than 500 students.')
    print(f'To verify the sum of responses to "school enrollment": {sum_of_respondants_to_enroll}')
    print(summary_of_respondants_to_enroll)
    print()

#SCHLEVEL_y = Q: School Level (3 categories)
#SCHLEVEL_y = A: 1 = "Elementary", 2 = "Secondary", 3 = "Combined"
def schlvl():
    Elementary =        df1[  (df1['SCHLEVEL_y']==1)  ]
    total_Elementary =  Elementary.shape[0]
    Secondary =         df1[  (df1['SCHLEVEL_y']==2)  ]
    total_Secondary =   Secondary.shape[0]
    Combined =          df1[  (df1['SCHLEVEL_y']==3)  ]
    total_Combined =    Combined.shape[0]

    sum_of_respondants_to_schlvl = np.sum(total_Elementary + total_Secondary + total_Combined)
    summary_of_respondants_to_schlvl = df1[ "SCHLEVEL_y" ].describe()

    print("School level based on school reported grade levels offered.")
    it = "There are"
    print(f'{it} {total_Elementary} elementary level schools: a school that has any of grades K-6 and none of grades 9-12.')
    print(f'{it} {total_Secondary} secondary level schools: a school that has any of grades 7-12 and none of grades K-6.')
    print(f'{it} {total_Combined} combined level schools: for all other cases.')
    print(f'To verify the sum of responses to "school level": {sum_of_respondants_to_schlvl}')
    print(summary_of_respondants_to_schlvl)
    print()

#ATTACK = Q: Has the teacher ever been physically attacked by a student?
#ATTACK = A: 0 = Never attacked, 1 = Attacked, but not in past 12 months, 2 = Attacked in past 12 months
def smite():
    fine = df1[ (df1['ATTACK']==0)  ]
    total_fine = fine.shape[0]
    bruise = df1[  (df1['ATTACK']==1)  ]
    total_bruise = bruise.shape[0]
    hurt = df1[  (df1['ATTACK']==2)  ]
    total_hurt = hurt.shape[0]

    sum_of_respondants_to_smite = np.sum(total_fine + total_bruise + total_hurt)
    summary_of_respondants_to_smite = df1[ "ATTACK" ].describe()

    print("Has the teacher ever been physically attacked by a student?")
    print(f'Total number of teachers that have never been attacked: {total_fine}')
    print(f'Total number of teachers that have been attacked, but not in the last 12 months: {total_bruise}')
    print(f'Total number of teachers that have been attacked in the past 12 months: {total_hurt}')
    print(f'To verify the sum of responses to "teacher ever being attacked": {sum_of_respondants_to_smite}')
    print(summary_of_respondants_to_smite)
    print()







