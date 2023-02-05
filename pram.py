# Ammar Taha, original: 01/02/2023, last update: 01/02/2023
# post randomization method, get probabilities of categorical data and replace original values using this probability
# categorie ci has probability of 0 <= pi <= 1, sum pi = 1
# telecom_customer_churn.csv Offer
import pandas as pd
import random 

def pram(original, masked, column): # path of original data, name of new masked data file, column to change
    size = 20 # size of entries to test on
    df = pd.read_csv(original) # data frame
    pd.set_option('display.max_columns', 100) # set max size of number of columns to show
    print(df.shape) # print shape of Dataframe
    new_df = df.head(size) # make new dataframe of first n = size values 
    o_values = new_df[column].values.tolist() # make list of original values
    m_values = [] # make list of masked values
    names = ['Original Data', 'Masked Data']
    categories = {} # Data structures to track data
    probabilities = []
    cat = []
    total = 0
    cumulative_p = 0
    
    for index, row in new_df.iterrows(): # track frequeny of original data by using dictionary with categorie:frequency as key:value pairs
        dkey = row[column]
        if dkey in categories:
            categories.update({dkey:categories[dkey]+1})
            total += 1
        else:
            categories[dkey] = 1
            total += 1
    
    for k, v in categories.items(): # get probabilties and cummulative probability
        cumulative_p += v/total
        categories[k] = v/total
        probabilities.append(cumulative_p)
        cat.append(k)
    for index, row in new_df.iterrows(): # generate masked data based on probability
        roll = random.random()
        for i in range(len(probabilities)):
            if roll <= probabilities[i]:
                new_df.loc[index, [column]] = cat[i]
                break

    m_values = new_df[column].values.tolist()
    new_df.to_csv(masked) # save dataframe to csv file
    # finally make new dataframe to show original values, percentages and masked values
    Display_df = pd.DataFrame(list(zip(o_values, m_values)), columns = names) 
    print(Display_df)

pram('D:\stuff\School\CS_year_5\Graduation project\datamasking\\test_data\\telecom_customer_churn_prediction\\telecom_customer_churn.csv', 'pram_offer_data.csv', 'Offer')
