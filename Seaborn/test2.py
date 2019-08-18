# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:55:17 2019

@author: Arunn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Path of the file to read
filepath = "Mall_Customers.csv"

# Read the file into a variable fifa_data
mall_data = pd.read_csv(filepath,index_col="CustomerID")
mall_data.head()

plt.figure(figsize=(16,6))

sns.regplot(x=mall_data["Age"], y=mall_data["Income"])

sns.lineplot(data=mall_data["Age"])

sns.distplot(a=mall_data["Age"], kde=False)

# KDE plot 
sns.kdeplot(data=mall_data["Age"], shade=True)
sns.kdeplot(data=mall_data["Income"], shade=True)

# 2D KDE plot
sns.jointplot(x=mall_data["Age"], y=mall_data["Income"], kind="kde")

