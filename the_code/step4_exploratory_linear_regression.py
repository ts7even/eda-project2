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
df1['NEW_STATUS'] = df1.STATUS.map({'L':1, 'M':2, 'S':3})
# df2 = df1[['NEW_STATUS']]


def summaryStatsdependent():
    dependent_variable = df1['NEW_STATUS']
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
    school_lvl_independent_variable = df1['SCHLEVEL_x'].describe()
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
    plt.savefig('profiling/graph_mentor_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphingAttackIndependentVariable():
    attack_histogram = df1['ATTACK']
    plt.hist(attack_histogram)
    plt.title("Where you attacked by a student?")
    plt.ylabel("Observations")
    plt.xticks([0,1,2], ['Never Attacked', 'Not attacked in the last 12 months', 'Attacked in the last 12 months'])
    plt.savefig('profiling/graph_attack_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphingAgeIndependentVariable():
    age_histogram = df1['AGE_T']
    plt.hist(age_histogram)
    plt.title("What is the Teacher Age?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3,4], ['< 30', '30 - 39', '40-49', '50 >'])
    plt.savefig('profiling/graph_age_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphingGenderIndependentVariable():
    gender_histogram = df1['T0356']
    plt.hist(gender_histogram)
    plt.title("What is the Teacher Gender?")
    plt.ylabel("Observations")
    plt.xticks([1,2], ['Male', 'Female'])
    plt.savefig('profiling/graph_gender_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphingRaceIndependentVariable():
    race_histogram = df1['RACETH_T']
    plt.hist(race_histogram)
    plt.title("What is the Teacher's race?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3,4,5], ['American Indian', 'Asian', 'Black', 'White', 'Hispanic'])
    plt.savefig('profiling/graph_race_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphingSchlevelIndependentVariable():
    schlevel_histogram = df1['SCHLEVEL_x']
    plt.hist(schlevel_histogram)
    plt.title("What kind of school does the teacher teach?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3], ['Elementary', 'Secondary', 'Combined'])
    plt.savefig('profiling/graph_schlevel_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphingEnrollmentIndependentVariable():
    enrollment_histogram = df1['S0101']
    plt.hist(enrollment_histogram)
    plt.title("What is the total enrollment?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3], ['< 300', '300 - 499', '500 >'])
    plt.savefig('profiling/graph_enrollment_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphingAssignIndependentVariable():
    assign_histogram = df1['ASSIGN']
    plt.hist(assign_histogram)
    plt.title("What is the teachers assignment?")
    plt.ylabel("Observations")
    plt.xticks([1,2,3,4,5,6,7,8,9], ['general-elementary', 'Math and Science', 'English','Social Science', 'Special Education', 'Foreign Language', 'ESL Education', 'Vocational', 'All Others'])
    plt.savefig('profiling/graph_assigment_hist.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def graphTwoVariables(): # Step 3
    #  Simple Linear Regression
    clean_yaxis = df1[(df1['STATUS']=='L')].dropna() # Dependent Variable:  Leaver 
    yaxis = df1['NEW_STATUS']
    xaxis = df1['ASSIGN']# Independent variable of experiance
    # print(yaxis.head)
    # print(xaxis.head)
    plt.scatter(xaxis, yaxis)
    plt.title("What is the teachers assignment when leaving?")
    plt.xticks()
    plt.ylabel('Left Teaching')
    plt.savefig('profiling/graph_assignment.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()


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
    plt.savefig('profiling/sale_price_lot_size.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def simpleRegression():
    x = df1['AGE_T']
    y = df1['NEW_STATUS']

    model = smf.ols('NEW_STATUS ~ AGE_T', data=df1)
    model = model.fit()
    prediction = model.predict()
    print('Single Simple Regression Summary')
    print(model.summary())
    print()

    plt.plot(x, y, 'o')
    plt.plot(x, prediction, 'r', linewidth=2)
    plt.xlabel('Teacher Ages')
    plt.ylabel('Teacher Status')
    plt.title('Teacher Status vs Age')
    plt.savefig('profiling/teacher_status_vs_age.png')
    plt.show(block=False)
    plt.pause(2)
    plt.close()


def multiRegression():
    x1 = df1['RACETH_T']
    x2 = df1['ASSIGN']
    x3 = df1['TOTEXPER']
    x4 = df1['S0101']


    y = df1['NEW_STATUS']
    # x = x1, x2, x3, x4
    # Summary Stats or Regression
    model = smf.ols('NEW_STATUS ~ RACETH_T + ASSIGN + TOTEXPER + S0101', data=df1)
    model = model.fit()
    prediction = model.predict()
    print('Multiple Regression Summary')
    print(model.summary())
    print()
    print("For RACETH_T significance is .44 which is too high to make a conclusion about the data; this is becasue we nedd a value of less than .05 to be sure that the variable has an effect on the thing we are measuring. Sign is positive. Size is 3823 observasions. ")
    print("For ASSIGN significance is .015 which is too high to make a conclusion about the data; this is becasue we nedd a value of less than .05 to be sure that the variable has an effect on the thing we are measuring. Sign is positive. Size is 3823 observasions.  ")
    print("For TOTEXPER significance is .107 which is too high to make a conclusion about the data; this is becasue we nedd a value of less than .05 to be sure that the variable has an effect on the thing we are measuring. Sign is positive. Size is 3823 observasions.  ")
    print("For S0101 significance is .077 which is too high to make a conclusion about the data; this is becasue we nedd a value of less than .05 to be sure that the variable has an effect on the thing we are measuring. Sign is positive. Size is 3823 observasions. ")



def profiler():
    df = df1[['STATUS', 'NEW_STATUS', 'ASSIGN', 'SCHLEVEL_x', 'T0356', 'RACETH_T', 'TOTEXPER', 'T0149','ATTACK', 'AGE_T', 'S0101']]
    profile = ProfileReport(df, title='Graphing Variable Profile', minimal=True)
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
# graphingAssignIndependentVariable() # 
# graphTwoVariables() 
# exampleRegression()
# simpleRegression()
# multiRegression() # Need Help
# profiler()




