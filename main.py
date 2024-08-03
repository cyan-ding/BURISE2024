import numpy as np
from scipy import stats
import pandas as pd
from matplotlib import pyplot as plt
from pingouin import mixed_anova
from statsmodels.stats.anova import AnovaRM

pcData = pd.read_csv("./exp_data/Project Data - PC Avg.csv", delimiter=",")
onData = pd.read_csv("./exp_data/Project Data - EXP-ON Avg.csv",delimiter=",")
offData = pd.read_csv("./exp_data/Project Data - EXP-OFF Avg.csv", delimiter=",")

def extractData(data, sex):
    spec_cols = [col for col in data.columns if sex in col]
    total_data = []
    for col in spec_cols:
        total_data.append(data[col])
    return total_data

data = {
    "Trial Number": [],
    "Time": [],
    "Average Climbing Activity": [],
    "Condition": [],
    "Sex": []
}

trial_numbers = list(range(1, 31))
times = [0.5, 1, 1.5, 2, 2.5, 3]
conditions = ["Control", "Serotonin On", "Serotonin Off"]
sexes = ["Male", "Female"]

avg_climbing_activity_data = {
    ("Control", "Male"): [extractData(pcData, "Male")],
    ("Control", "Female"): [extractData(pcData, "Female")],
    ("Serotonin On", "Male"): [extractData(onData, "Male")],
    ("Serotonin On", "Female"): [extractData(onData, "Female")],
    ("Serotonin Off", "Male"): [extractData(offData, "Male")],
    ("Serotonin Off", "Female"): [extractData(offData, "Female")]
}


print(avg_climbing_activity_data)

# for condition in conditions:
#     for sex in sexes:
#         for trial_number in trial_numbers:
#             for time in times:
#                 avg_activity = avg_climbing_activity_data[(condition, sex)]

# df = pd.DataFrame(avg_climbing_activity_data)

# print(df.head)