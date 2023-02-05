# Ammar Taha, 29/01/2023
# additive noise algorithm on telecom churn(cell2cell)
# add or subtract random noise between 0 - p% of original value, recommended 5 <= percent <= 10
# cell2cellholdout.csv Monthly Revenue 
import numpy as np
import pandas as pd
import random 
# import csv

def addNoise(percent, original, masked, column): # percent of noise, path of original data, name of new masked data file, column to change
    size = 20 # size of entries to test on
    df = pd.read_csv(original) # data frame
    pd.set_option('display.max_columns', 100)
    print(df.shape)
    df.info()
    print(df.head(size)[column]) # original column values
    new_df = df.head(size)
    for index, row in new_df.iterrows():
        s = round(100-percent + random.random()*2*percent, 2)  # additive noise
        print(s) # masked value as percent of original value
        new_df.loc[index, [column]] = [round(row[column]*s/100, 2)]

    new_df.to_csv(masked)
    print(new_df[column])

addNoise(8, 'D:\stuff\School\CS_year_5\Graduation project\datamasking\\test_data\\telecom_churn_cell2cell\cell2cellholdout.csv', 'added_noise_monthly_revenue.csv', 'MonthlyRevenue')




