import matplotlib
import pandas as pd
import numpy as np 
import pandas_profiling 
from pandas_profiling import ProfileReport
import scipy as sp
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf


# try pands profiling for report
# Linear Regression can only be used with Continuous Variables (Measured by goodnes of fit by loss, R-Squared, Adjusted R)
# Logistic Regression can be used with Categorical Variables (Measued by goodness of fit with Accuracy, Precision, Recall, F1 Score, ROC, Curve, Confusion Matrix, etc)

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
    expericance_independent_variable = df1['TOTEXPER'].describe() #Continuous
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

def graphingAgeIndependentVariable():
    age_histogram = df1['AGE_T']
    plt.hist(age_histogram)
    plt.title("What is the Teacher Age?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3,4], ['< 30', '30 - 39', '40-49', '50 >'])
    plt.show()

def graphingGenderIndependentVariable():
    gender_histogram = df1['T0356']
    plt.hist(gender_histogram)
    plt.title("What is the Teacher Gender?")
    plt.ylabel("Observations")
    plt.xticks([1,2], ['Male', 'Female'])
    plt.show()

def graphingRaceIndependentVariable():
    race_histogram = df1['RACETH_T']
    plt.hist(race_histogram)
    plt.title("What is the Teacher's race?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3,4,5], ['American Indian', 'Asian', 'Black', 'White', 'Hispanic'])
    plt.show()

def graphingSchlevelIndependentVariable():
    schlevel_histogram = df1['SCHLEVEL_y']
    plt.hist(schlevel_histogram)
    plt.title("What kind of school does the teacher teach?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3], ['Elementary', 'Secondary', 'Combined'])
    plt.show()

def graphingEnrollmentIndependentVariable():
    enrollment_histogram = df1['S0101']
    plt.hist(enrollment_histogram)
    plt.title("What is the total enrollment?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3], ['< 300', '300 - 499', '500 >'])
    plt.show()

def graphingAssignIndependentVariable():
    assign_histogram = df1['ASSIGN']
    plt.hist(assign_histogram)
    plt.title("What is the teachers assignment?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3,4,5,6,7,8,9], ['general-elementary', 'Math and Science', 'English','Social Science', 'Special Education', 'Foreign Language', 'ESL Education', 'Vocational', 'All Others'])
    plt.show()

def graphTwoVariables(): # Step 3
    #  Simple Linear Regression
    clean_yaxis = df1[(df1['STATUS']=='L')].dropna() # Dependent Variable:  Leaver 
    yaxis = clean_yaxis['STATUS']
    xaxis = clean_yaxis['ASSIGN']# Independent variable of experiance
    # print(yaxis.head)
    # print(xaxis.head)
    plt.hist(xaxis)
    plt.title("What is the teachers assignment when leaving?")
    plt.xticks([1,2,3,4,5,6,7,8,9], ['general-elementary', 'Math and Science', 'English','Social Science', 'Special Education', 'Foreign Language', 'ESL Education', 'Vocational', 'All Others'])
    plt.ylabel('Left Teaching')
    plt.show()


def exampleRegression():
    # Simple Single Linear Regression using statsmodels and matplotlib
    df = pd.read_excel('source/datasets/HPRICE.xlsx')

    y = df['saleprice']
    x = df['lotsize']

    model = smf.ols('saleprice ~ lotsize', data=df)
    model = model.fit()
    price_pred = model.predict()


    plt.plot(x, y, 'o')
    plt.plot(x, price_pred, 'r', linewidth=2)
    plt.xlabel('Lot Size')
    plt.ylabel('Sale Price')
    plt.title('Sales Price vs Lotsize')
    plt.show()



def profiler():
    df = df1[['STATUS', 'ASSIGN', 'SCHLEVEL_y', 'T0356']]
    profile = ProfileReport(df, title='Mutiple Variable Profile', minimal=True)
    profile.to_file('profiling/project-profiling.html')

# summaryStatsdependent()
# summaryStatsindependent()
# graphingMentorIndependentVariable()
# graphingAttackIndependentVariable()
# graphingAgeIndependentVariable()
# graphingGenderIndependentVariable()
# graphingRaceIndependentVariable()
# graphingSchlevelIndependentVariable()
# graphingEnrollmentIndependentVariable()
# graphingAssignIndependentVariable() - Not Happy with this one
# graphTwoVariables() - Not Happy with this one
# exampleRegression()
# profiler()





# Drop NA amount of teacher that left is 1544
# Problem-drug abuse #T0330
# Problem Disrespect for Teachers #T0332
# Sch yr-amount tchr pay # T0347
# Grade Level of Students Taught by Teacher #TEALEV
# New teacher flag # NEWTEACH


