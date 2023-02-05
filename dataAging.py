# Ammar Taha, original: 31/01/2023, last update: 01/02/2023
# Change date on Worldcall Telecom Limited
# change date within 0 to d days, 0 to m months, 0 to y years
# worldcall_telecom_limited WTL.csv date
import pandas as pd
import datetime
import random 

def changeDate(range_y, range_m, range_d, original, masked, column): # year, months, days, path of original data, name of new masked data file, column to change
    size = 20 # size of entries to test on
    d_parser = lambda x: pd.datetime.strptime(x, '%d/%m/%Y %H:%M') # create date parser using lambda function to turn default object into datetime type 
    df = pd.read_csv(original, parse_dates=[column], date_parser=d_parser) # load in original data while turning date object to datetime object
    pd.set_option('display.max_columns', 100) # set max size of number of columns to show
    print(df.shape) # print shape of Dataframe
    new_df = df.head(size) # make new dataframe of first n = size values 
    o_values = [] # new_df[column].values.tolist() # make list of original values
    change = [] # make list of changes in date 
    m_values = [] # make list of masked values
    names = ['Original Data', 'Change', 'Masked Data']

    for index, row in new_df.iterrows():
        days = random.randint(0, range_d) # range to change days by
        months = random.randint(0, range_m) # range to change months by
        years = random.randint(0, range_y) # range to change years by
        d_sign = 1 # default days sign
        m_sign = 1 # default months sign
        y_sign = 1 # default years sign
        # deside add or subtract from value
        d_r = random.random()
        m_r = random.random()
        y_r = random.random()
        if (d_r < 0.5):
            d_sign = -1
        if (m_r < 0.5):
            m_sign = -1
        if (y_r < 0.5):
            y_sign = -1
        signed_days = (days * d_sign)
        signed_months = (months * m_sign)
        signed_years = (years * y_sign)
        o_values.append(row[column])
        
        # add values and keep integrity of date
        new_month = (row[column].month+signed_months+12)%12
        if new_month == 0: 
            new_month = 12
        new_year = row[column].year+signed_years
        if (new_month == 1, 3, 5, 7, 8, 10, 12):
            new_day = (row[column].day+signed_days+31)%31
            if new_day == 0: 
                new_day = 31
        elif (new_month == 4, 6, 9, 11):
            new_day = (row[column].day+signed_days+30)%30
            if new_day == 0: 
                new_day = 30
        elif (new_month == 2):
            if (row[column].is_leap_year):
                new_day = (row[column].day+signed_days+29)%29
                if new_day == 0: 
                    new_day = 29
            else:
                new_day = (row[column].day+signed_days+28)%28
                if new_day == 0: 
                    new_day = 28

        new_date = datetime.datetime(year=new_year, month= new_month, day=new_day) # make new date
        new_df.loc[index, [column]] = new_date
        change.append([signed_years, signed_months, signed_days])

    for index, row in new_df.iterrows(): # append masked dates to m_values
        m_values.append(row[column])
    
    new_df.to_csv(masked) # save dataframe to csv file
    # finally make new dataframe to show original values, changes and masked values
    Display_df = pd.DataFrame(list(zip(o_values, change, m_values)), columns = names) 
    print(Display_df)

changeDate(2, 5, 10, 'D:\stuff\School\CS_year_5\Graduation project\datamasking\\test_data\worldcall_telecom_limited\WTL.csv', 'date_changed_data.csv', 'date')

