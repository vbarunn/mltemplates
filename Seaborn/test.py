# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Path of the file to read
fifa_filepath = "data.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath,index_col="ts")
fifa_data.head()

plt.figure(figsize=(16,6))
sns.lineplot(data=fifa_data["tp"])
sns.lineplot(data=fifa_data["hm"])

fifa_data1=fifa_data.loc[:, ['tp','hm','lgt']]

sns.regplot(x=fifa_data1['tp'], y=fifa_data1['hm'])

sns.regplot(x=fifa_data1['tp'], y=fifa_data1['lgt'])

sns.regplot(x=fifa_data1['hm'], y=fifa_data1['lgt'])


