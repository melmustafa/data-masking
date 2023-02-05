# Ammar Taha, original: 31/01/2023, last update: 01/02/2023
# micro aggregate on on small clusters in Telecom Customer Churn Prediction
# get aggregate (mean) of clusters of size cluster_size
# telecom_customer_churn.csv Age
import pandas as pd

def microAggregate(cluster_size, original, masked, column): # size of cluster, path of original data, name of new masked data file, column to change
    size = 23 # size of entries to test on
    df = pd.read_csv(original) # data frame
    pd.set_option('display.max_columns', 100) # set max size of number of columns to show
    print('Data shape: ', df.shape) # print shape of Dataframe
    new_df = df.head(size) # make new dataframe of first n = size values 
    o_values = new_df[column].values.tolist() # make list of original values
    m_values = [] # make list of masked values
    names = ['Original Data', 'Masked Data']

    # values to calculate cluster aggregate
    current_mean = 0
    current_total = 0
    remainder = 0
    means = []
    for index, row in new_df.iterrows():
        if ((index+1) % cluster_size != 0):
            current_total += row[column]
            remainder += 1
        else:
            current_mean = current_total / cluster_size
            means.append(current_mean)
            current_mean = 0
            current_total = 0
            remainder = 0
    if (remainder != 0):
        current_mean = current_total / remainder
        means.append(current_mean)
        current_mean = 0
        current_total = 0

    for index, row in new_df.iterrows():
        new_df.loc[index, [column]] = means[index//cluster_size]
        m_values.append(new_df.loc[index, column])

    new_df.to_csv(masked) # save dataframe to csv file
    # finally make new dataframe to show original values, percentages and masked values
    Display_df = pd.DataFrame(list(zip(o_values, m_values)), columns = names) 
    print(Display_df)

microAggregate(5, 'D:\stuff\School\CS_year_5\Graduation project\datamasking\\test_data\\telecom_customer_churn_prediction\\telecom_customer_churn.csv', 'micro_aggregated_customer_age.csv', 'Age')
