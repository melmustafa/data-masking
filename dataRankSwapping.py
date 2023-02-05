# Ammar Taha, 30/01/2023
# Data Rank Swapping on Telecom Customer
# swap ranks of data within 0 to n ranks
# Telecom_customer churn.csv ethnicity 
import numpy as np
import pandas as pd
import random 
# import csv

def swapRank(range, original, masked, column): # range of rank swapping, path of original data, name of new masked data file, column to change
    size = 20 # size of entries to test on
    df = pd.read_csv(original) # data frame 
    pd.set_option('display.max_columns', 100)
    print(df.shape)
    df.info()
    print(df.head(size)[column]) # original column values
    new_df = df.head(size)
    for index, row in new_df.iterrows():
        rank = random.randint(1, range) # range to swap ranks by
        sign = 1 # default sign
        r = random.random()
        if (r < 0.5):
            sign = -1
        signed_rank = (rank * sign)
        print(signed_rank) # signed rank to swap by
        if (index + signed_rank >= 0) and (index + signed_rank < size): # if range of swap is valid continue
            # if (new_df.loc[index, [column]].to_string(index=False, header=False) == df.loc[index, [column]].to_string(index=False, header=False)): # check if this value has been swapped
            temp = new_df.loc[index, [column]] 
            new_df.loc[index, [column]] = df.loc[index + signed_rank, [column]]
            new_df.loc[index + signed_rank, [column]] = temp

    new_df.to_csv(masked)
    print(new_df[column])

swapRank(5, 'D:\stuff\School\CS_year_5\Graduation project\datamasking\\test_data\\telecom_customer\Telecom_customer churn.csv', 'swapped_rank_ethnicity.csv', 'ethnic')

