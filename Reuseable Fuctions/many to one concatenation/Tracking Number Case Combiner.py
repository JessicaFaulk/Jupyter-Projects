#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd
import numpy as np
import datetime as dt
import datetime

def concat_cases(filename):
    df = pd.read_excel(filename, parse_dates=['Intake Date'])
    df = df.loc[(df['Respondent Agency'] =='DSHS')]
    df['Closed Date'] = df['Closed Date'].fillna('1-1-1900')
    df['Closed Date'] = pd.to_datetime(df['Closed Date'])
    # concatenate the string 
    df['Tracking Number'] = df['Tracking Number'].astype('string').str.title()
    df['Finding'] = df['Finding'].astype('string').str.title()
    df['Discrimination'] = df['Discrimination'].astype('string').str.title()
    df['Issues'] = df['Issues'].astype('string').str.title()
    df['Other Issue'] = df['Other Issue'].astype('string').str.title()
    df['Disability'] = df['Disability'].astype('string').str.title()
    df['Other Disability'] = df['Other Disability'].astype('string').str.title()
    df['Status'] = df['Status'].astype('string').str.title()
    df['Case Type'] = df['Case Type'].astype('string').str.title()
    df['Intake Date formatted m/d/y'] = df["Intake Date"].map(lambda ts: ts.strftime("%m-%d-%Y"))
    df['Closed Date formatted m/d/y'] = df["Closed Date"].map(lambda ts: ts.strftime("%m-%d-%Y"))

    g_descrim = df.groupby('Tracking Number')['Discrimination'].unique().apply(list)
    g_disabil = df.groupby('Tracking Number')['Disability'].unique().apply(list)
    g_disabil_ot = df.groupby('Tracking Number')['Other Disability'].unique().apply(list)
    g_issue = df.groupby('Tracking Number')['Issues'].unique().apply(list)
    g_issue_ot=df.groupby('Tracking Number')['Other Issue'].unique().apply(list)
    g_status = df.groupby('Tracking Number')['Status'].unique().apply(list)
    g_case = df.groupby('Tracking Number')['Case Type'].unique().apply(list)
    g_find = df.groupby('Tracking Number')['Finding'].unique().apply(list)
    g_result = df.groupby('Tracking Number')['Result'].unique().apply(list)
    g_result_ot=df.groupby('Tracking Number')['Other Result'].unique().apply(list)
    g_agency = df.groupby('Tracking Number')['Respondent Agency'].unique().apply(list)
    g_intake_date = df.groupby('Tracking Number')['Intake Date formatted m/d/y'].unique().apply(list)
    g_closed_date = df.groupby('Tracking Number')['Closed Date formatted m/d/y'].unique().apply(list)

    #create new frame
    df_1TNo = pd.concat([g_case,g_descrim,g_disabil,g_disabil_ot,g_issue,g_issue_ot,g_status,g_find,g_result,g_result_ot,g_agency, g_intake_date, g_closed_date], axis=1).reset_index()
    df_1TNo
    df_1TNo.to_excel('Combined Cases.xlsx')
    print('done')
filename = input('Input the filepath: ')
concat_cases(filename)


# In[98]:





# In[ ]:




