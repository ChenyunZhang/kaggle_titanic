import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("data/train.csv")
train_data = pd.read_csv("data/test.csv")
print(f"header: {train_data.head()}")

# .loc[] is primarily label based, but may also be used with a boolean array.

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = round(sum(women)/len(women),2)

print(f"% of women who survived:{rate_women}")

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = round(sum(men)/len(men),2)

print(f"% of men who survived:{rate_men}")

