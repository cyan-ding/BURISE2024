import numpy as np
from scipy.stats import shapiro
from scipy.stats import skew
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from statsmodels.formula.api import mixedlm

pcData = pd.read_csv("./exp_data/Project Data - PC Avg.csv", delimiter=",")
onData = pd.read_csv("./exp_data/Project Data - EXP-ON Avg.csv",delimiter=",")
offData = pd.read_csv("./exp_data/Project Data - EXP-OFF Avg.csv", delimiter=",")

def extractData(data, sex):
    spec_cols = [col for col in data.columns if sex in col]
    return data[spec_cols]

# print(extractData(pcData, "Male")["Hour 1 Male Means"].mean())

def graph(data, sex, x_label, y_label, title, fmt):
    axis = [0.5, 1, 1.5, 2, 2.5, 3]
    mean = extractData(data, sex).mean()
    error = extractData(data, sex).sem()
    plt.plot(axis, mean, fmt)
    plt.errorbar(axis, mean, error, ecolor = "black")
    plt.xlabel(xlabel=x_label), plt.ylabel(ylabel=y_label), plt.title(title, loc='center')
    


l1 = graph(pcData, "Male", "Hours", "Average Quadrant", "Sex Difference PC", 'bo-')
l2 = graph(pcData, "Female", "Hours", "Average Quadrant", "Sex Difference PC", "ro-")

# l3 = graph(offData, "Female", "Hours", "Average Quadrant", "Female", "go-")

blue_patch = mpatches.Patch(color='blue', label='Male')
red_patch = mpatches.Patch(color='red', label='Female')
# green_patch = mpatches.Patch(color='green', label='OFF')
plt.legend(handles=[blue_patch, red_patch])


plt.show()


# Data Analysis 

# data = {
#     "Time": [],
#     "AverageClimbingActivity": [],
#     "Condition": [],
#     "Sex": [],
#     "Group": []
# }


# times = [0.5, 1, 1.5, 2, 2.5, 3]
# conditions = ["Control", "Serotonin On", "Serotonin Off"]
# sexes = ["Male", "Female"]
# groups = [1, 2, 3, 4, 5, 6]







# avg_climbing_activity_data = {
#     ("Control", "Male"): (extractData(pcData, "Male"), 1),
#     ("Control", "Female"): (extractData(pcData, "Female"), 2),
#     ("Serotonin On", "Male"): (extractData(onData, "Male"), 3),
#     ("Serotonin On", "Female"): (extractData(onData, "Female"), 4),
#     ("Serotonin Off", "Male"): (extractData(offData, "Male"), 5),
#     ("Serotonin Off", "Female"): (extractData(offData, "Female"), 6)
# }



# for condition in conditions:
#     for sex in sexes:
#         for time in times:
#             for trial in range(30):
#                 str = f"Hour {time} {sex} Means"
#                 avg_activity = avg_climbing_activity_data[(condition, sex)][0][str][trial]
#                 data['Time'].append(time)
#                 data['AverageClimbingActivity'].append(avg_activity)
#                 data['Condition'].append(condition)
#                 data['Sex'].append(sex)
#                 data['Group'].append(avg_climbing_activity_data[(condition, sex)][-1])


# df = pd.DataFrame(data)


# df.dropna(inplace=True)

# df['Condition'] = df['Condition'].astype('category')
# df['Sex'] = df['Sex'].astype('category')
# df['Group'] = df['Group'].astype('category')

# formula = "AverageClimbingActivity ~ Condition * Sex * Time"


# model = mixedlm(formula, df, groups=df["Group"], re_formula="~Time")
# result = model.fit()

# print(result.summary())


