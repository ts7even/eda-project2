import matplotlib
import pandas as pd
import numpy as np 
import pandas_profiling as pp
import scipy as sp
import matplotlib.pyplot as plt



df1 = pd.read_csv('source/merge/data-merge2.csv', low_memory=False)


def summaryStatsdependent():
    dependent_variable = df1['STATUS']
    describe_dependent_variable = dependent_variable.describe()
    print('The summary stats for the dependent variable...')
    print(describe_dependent_variable)
    print()


def summaryStatsindependent():
    age_independent_variable = df1['AGE_T'].describe()
    sex_independent_variable = df1['T0356'].describe()
    race_independent_variable = df1['RACETH_T'].describe()
    expericance_independent_variable = df1['TOTEXPER'].describe()
    assign_independent_variable = df1['ASSIGN'].describe()
    mentor_independent_varable = df1[(df1['T0149']!=-8)]
    cleaned_mentor_independent_variable = mentor_independent_varable['T0149'].describe()
    enrollment_independent_variable = df1['S0101'].describe()
    school_lvl_independent_variable = df1['SCHLEVEL_y'].describe()
    attack_independent_variable = df1['ATTACK'].describe()
    print('Summary stats for age')
    print(age_independent_variable)
    print()
    print('Summary Stats for sex')
    print(sex_independent_variable)
    print()
    print('Summary Stats for race')
    print(race_independent_variable)
    print()
    print('Summary stats for experiance')
    print(expericance_independent_variable)
    print()
    print('Summary stats for techer assignment')
    print(assign_independent_variable)
    print()
    print('Summary stats for mentorship')
    print(cleaned_mentor_independent_variable)
    print()
    print('Summary stats for enrollment size')
    print(enrollment_independent_variable)
    print()
    print('Summary Stats for school level ')
    print(school_lvl_independent_variable)
    print()
    print('Summary stats for attaked teachers')
    print(attack_independent_variable)
    print()


matplotlib.use('Qt5Agg')

def graphingMentorIndependentVariable():
    mentor_histogram = df1[(df1['T0149']!=-8)]
    filtered_mentor_histogram = mentor_histogram[['T0149']]
    plt.hist(filtered_mentor_histogram)
    plt.title("Mentor Independent Variable")
    plt.ylabel("Observations")
    plt.xticks([1,2,3,4,5], ['Not at All', 'Little Extent', 'To Some Extent', 'To a Good Extend', 'To a Great Extent'])
    plt.show()

def graphingAttackIndependentVariable():
    attack_histogram = df1['ATTACK']
    plt.hist(attack_histogram)
    plt.title("Where you attacked by a student?")
    plt.ylabel("Observations")
    plt.xticks([0,1,2], ['Never Attacked', 'Not attacked in the last 12 months', 'Attacked in the last 12 months'])
    plt.show()

 
# summaryStatsdependent()
# summaryStatsindependent()
# graphingMentorIndependentVariable()
# graphingAttackIndependentVariable()