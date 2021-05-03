#!/usr/bin/env python
# coding: utf-8

# # CAPSTONE TWO: NEGATIVE INCOME TAX EXPERIMENTS

# ## IMPORTS

# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
pd.options.display.width=None
pd.options.display.max_colwidth=10000
pd.options.display.max_columns = 10000
pd.options.display.max_rows = 100


# In[3]:


gary_df = pd.read_csv('../data/raw/raw_gary_df.csv', dtype=str)
gary_df.drop('Unnamed: 0', axis=1, inplace=True)
gary_df.dropna(inplace=True)


# ### WIDE DATA -> LONG DATA

# In[4]:


def chunkstring(string, length):
    return [string[0+i:length+i] for i in range(0, len(string), length)]
def stub_maker(df, list_of_lengths):
    col_dict = {}
    stub_dict = {}
    for length in list_of_lengths:
        col_dict[length] = [col for col in df.columns if length in col]
    for length in col_dict:
        stub_cols = []
        for column in col_dict[length]:
            numeric_length = int(length[1:])
            if numeric_length == 73:
                numeric_length = 5
            stub = column.split('-')[0][:-1]
            stub_cols.append(stub)
            leng = int(df[column].str.len().unique() / numeric_length)
            df[column] = df[column].apply(chunkstring, args=[leng] )
        stub_dict[length] = stub_cols
    return stub_dict, col_dict
lengths = ['-48', '-42', '-9', '-16', '-73']


# In[5]:


stubs, cols = stub_maker(gary_df, lengths)


# In[6]:


tiles = list(np.arange(1, 49))*5326
test_df = gary_df.copy()
#test_df.assign(period48 = test_tile)
test_dict = {}
test_dict['-48'] = test_df.loc[:, [col for col in test_df if '48' in col]].apply(lambda x: x.explode())
test_dict['-48']['PERIOD'] = tiles
test_dict['-48']


# In[7]:


tiles = list(np.arange(0, 43))*5326
test_df = gary_df.copy()

test_dict['-42'] = test_df.loc[:, [col for col in test_df if '42' in col]].apply(lambda x: x.explode())
print(len(tiles), len(test_dict['-42']))
test_dict['-42']['PERIOD'] = tiles
test_dict['-42']


# In[8]:


tiles = list(np.arange(8, 49, 5))*5326
test_df = gary_df.copy()

test_dict['-9'] = test_df.loc[:, [col for col in test_df if '-9' in col]].apply(lambda x: x.explode())
print(len(tiles), len(test_dict['-9']))
test_dict['-9']['PERIOD'] = tiles
test_dict['-9']


# In[9]:


tiles = list(np.arange(3, 49, 3))*5326
test_df = gary_df.copy()

test_dict['-16'] = test_df.loc[:, [col for col in test_df if '16' in col]].apply(lambda x: x.explode())
test_dict['-16']['PERIOD'] = tiles
test_dict['-16']


# In[13]:


tiles = list(np.arange(1, 6))*5326
test_df = gary_df.copy()

test_dict['-73'] = test_df.loc[:, [col for col in test_df if '69-73' in col]].apply(lambda x: x.explode())
test_dict['-73']['PERIOD'] = tiles
test_dict['-73']


# In[ ]:


final_frame = pd.merge(test_dict['-42'], test_dict['-48'], on='PERIOD', how='left', sort=False)
final_frame.to_csv("../data/raw/gary_exploded.csv")


# In[ ]:


#gary_df.set_index('PERNUM', inplace = True)


# In[ ]:


# test =  np.arange(1,49,1)
# test_series = np.tile(test, (1,int(255648/48)))

#'''
#length = '-48'
#for length in lengths:
#numeric_length = -1 * int(length)
#gary_df['PER' + length] = [list(range(1,numeric_length ,1))] * len(gary_df)
#long_df = gary_df.loc[:, gary_df.columns.str.contains(length)]
#long_df.apply(pd.Series.explode)
#'''


# In[ ]:


# # tiles = list(np.arange(1, 49))*5326
# test_df = gary_df.copy()
# test_df.assign(period48 = test_tile)
# test_cols_list = [col for col in test_df.columns if '-42' in col or '-9' in col or '-73' in col]
# test_dict = {}
# test_dict['-48'] = test_df.loc[:, [col for col in test_df if '48' in col]].apply(lambda x: x.explode())
# test_dict['-48']['PERIOD-48'] = tiles
# test_dict['-48']


# In[ ]:


# cols = [col for col in gary_df.columns if '-42' in col]
# for col in cols:
#     lencols = gary_df[col].apply(len) - 43
#     print(lencols.sum())


# In[ ]:


# def exploder(df, list_of_lengths):
#     exploded_frames = {}
#     for length in list_of_lengths:
#         test_df = df.copy()
#         if length == '-73':
#             num_length = 5
#         elif length =='-42':
#             numeric_length = 43
#         else:
#             num_length = -1 * int(length)
#         values = list(np.arange(1, num_length+1)) * 5326
#         exploded_frames[length] = df.loc[:, [col for col in df if length in col]].apply(lambda x: x.explode())
#         print(values, exploded_frames[length])
#         exploded_frames[length]['PER' + length] = values
#     return exploded_frames
# gary_explode = exploder(gary_df, lengths)


# In[ ]:


# test_df = gary_df.copy()
# test =  np.arange(1,43,1)
# test_series = np.tile(test, (1,5326))
# test_dict = {}
# test_dict['-42'] = test_df.loc[:, [col for col in test_df.columns if '-42' in col]].apply(lambda x: x.explode())
# len(test_dict['-42'])
# len(test_series[0])


# In[ ]:


# list_cols = [col for col in test_df.columns if '-48' in col]
# test_dict['-48'] = test_df[list_cols].apply(pd.Series.explode)

# list_cols = [col for col in test_df.columns if '-42' in col]
# test_dict['-42'] = test_df[list_cols].apply(pd.Series.explode)

# list_cols = [col for col in test_df.columns if '-9' in col]
# test_dict['-9'] = test_df[list_cols].apply(pd.Series.explode)

# list_cols = [col for col in test_df.columns if '-16' in col]
# test_dict['-16'] = test_df[list_cols].apply(pd.Series.explode)

# list_cols = [col for col in test_df.columns if '-73' in col]
# test_dict['-73'] = test_df[list_cols].apply(pd.Series.explode)


# In[ ]:


# test_dict['-48']


# In[ ]:


# long_df


# In[ ]:



# for column in wide_cols:
#     if '-48' in column:
#         stubs48_split.append(column.split('-')[0])
#         leng = int(gary_df[column].str.len().unique() /48)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#         for i in range(48):
#             gary_df[column[:-4] + str(i+1)] = gary_df[column].apply(lambda x: x[i])
#     if '-42' in column:
#         stubs42_split.append(column.split('-')[0])
#         leng = int(gary_df[column].str.len().unique() /42)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#         for i in range(42):
#             gary_df[column[:-4] + str(i+1)] = gary_df[column].apply(lambda x: x[i])
#     if '-9' in column:
#         stubs9_split.append(column.split('-')[0])
#         leng = int(gary_df[column].str.len().unique() /9)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#         for i in range(9):
#             gary_df[column[:-3] + str(i+1)] = gary_df[column].apply(lambda x: x[i])  
#     if '-16' in column:
#         stubs16_split.append(column.split('-')[0])
#         leng = int(gary_df[column].str.len().unique() /16)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#         for i in range(16):      
#             gary_df[column[:-3] + str(i+1)] = gary_df[column].apply(lambda x: x[i])
#     if '-73' in column:
#         stubs5_split.append(column.split('-')[0])
#         leng = int(gary_df[column].str.len().unique() /5)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#         for i in range(5):
#             gary_df[column[:-3] + str(i+1)] = gary_df[column].apply(lambda x: x[i])


# In[ ]:


# gary_df.drop(wide_cols,axis=1, inplace=True)


# ### HANDLING NULLS

# dropping families with no people and people with no families (this was due to a record-keeping error on the part of the experimenters. Families starting with number 4 are supposed to be in the Sacramento file, not Gary).

# In[ ]:





# Converting some of the more-common missing data codes

# In[ ]:


# gary_df.replace(['9997', '9999','9993','9994', '97', '93'], np.NaN, inplace=True)


# dropping the columns with > 75% of their entries being left blank

# In[ ]:


# def percent_miss(df):
#     # returns the percent of entries that are None in each column.
#    return df.isnull().sum()/df.isnull().count()
# bad_cols = gary_df.loc[:,(percent_miss(gary_df) > 0.75)].columns
# gary_df.drop(bad_cols, axis=1, inplace= True)


# ATTDATE stands for attrition date, meaning what date the family left the experiment before it ended. These families left because they either moved away, stopped responding to experimenters, or the active filing member passed. They're being dropped here as we are interested in effects of welfare over time and these cutoff early.

# In[ ]:


# gary_df = gary_df.loc[gary_df['ATTDATE'] == '00000',:]
# gary_df.drop(['ATTDATE', 'FAMNUM'], axis=1, inplace=True)


# ## Encoding

# Many of the comments within this section are ideas for further analysis, or methods of data cleaning attempted that either failed or were too large of a time sink to complete.

# In[ ]:


#gary_df = gary_df.loc[gary_df['TREATLEV'] != '0']
#gary_control_df = gary_df.loc[gary_df['TREATLEV'] == '0']


# In[ ]:


# gary_df.set_index('PERNUM', inplace=True)
# gary_simp_df = pd.get_dummies(gary_df['TREATLEV'], drop_first=True)
# #gary_df.drop(['TREATLEV'], axis=1, inplace=True)
# col_dict = {1:'TREATLEV_1', 2: 'TREATLEV_2', 3:'TREATLEV_3', 4:'TREATLEV_4'}
# gary_simp_df.rename(columns = col_dict, inplace=True)


# In[ ]:


# gary_simp_df = pd.concat([gary_simp_df, pd.get_dummies(gary_df['POVLEV'], drop_first=True)], axis=1)
# #gary_df.drop(['POVLEV'], axis=1, inplace=True)
# col_dict = {2:'POV_LEV_2', 3: 'POV_LEV_3', 4:'POV_LEV_4', 5:'POV_LEV_5'}
# gary_simp_df.rename(columns = col_dict, inplace=True)


# This section of comments was my attempt to take the time-data and parse it out to hopefully generate new rows of data from them. Given more time, I would greatly expand this section, as it has the most potential and would give me the tools to make good features.

# In[ ]:


# '''def chunkstring(string, length):
#     return [string[0+i:length+i] for i in range(0, len(string), length)]
# for column in gary_df.columns:
#     if '-48' in column:
#         leng = int(gary_df[column].str.len().unique() /48)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#     if '-43' in column:
#         leng = int(gary_df[column].str.len().unique() /43)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#     if '-42' in column:
#         leng = int(gary_df[column].str.len().unique() /42)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#     if '-9' in column:
#         leng = int(gary_df[column].str.len().unique() /9)
#         gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
#  '''       


# In[ ]:


# '''
# for column in gary_df.columns:
#     if '-48' in column:
#         leng = int(gary_df[column].str.len().unique() /48)
#         basename = column
#         for i in range(48):
#             gary_df[basename+'-Month'+str(i)] = gary_df[column][i:i+leng]
# gary_df.head()
# '''


# Renaming the column for the sake of ease in coding.

# In[ ]:


# #gary_df.set_index('PERNUM', inplace=True)
# #periodic_columns =['SSI1-48', 'TTI1-48', 'SS1-48', 'VA1-48', 'MISINC1-48',
# #                   'OTHINC1-48', 'JOBINC1-48', 'DAYINC1-48', 'OJINC1-48',
# #                  'UEMBEN1-48', 'STRKWC1-48']
# gary_df.rename(columns= {'EMPSTAT1-9': 'EMPSTAT'}, inplace = True)
# gary_df.info


# Ruling out persons for which employment status data was never collected. 

# In[ ]:


# gary_simp_df['EMPSTAT'] = gary_df.loc[gary_df.EMPSTAT.str.contains('00|01|02', regex=True),'EMPSTAT']


# In[ ]:


# gary_simp_df.dropna(axis=0, inplace=True)


# Unemployed + Actively seeking work, Employed -> in the labor force -> 1   
# Unemployed + not actively seeking work -> not in labor force -> 0

# In[ ]:


# gary_simp_df.loc[(gary_simp_df.EMPSTAT.str.contains('(01)', regex=True)),'EMPSTAT']= '1'
# gary_simp_df.loc[(gary_simp_df.EMPSTAT.str.contains('(00)', regex=True)),'EMPSTAT']= '1'
# #gary_simp_df.loc[(gary_simp_df.EMPSTAT.str.contains('(00)(02)', regex=True)),'EMPSTAT']= 0


# In[ ]:


# gary_simp_df.loc[gary_simp_df['EMPSTAT'] != '1', 'EMPSTAT'] ='0'


# In[ ]:


# gary_simp_df


# ## MODELLING

# In[ ]:


# X= gary_simp_df.drop('EMPSTAT', axis=1)
# Y= gary_simp_df['EMPSTAT']
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=2, stratify = Y)
# print(y_train, y_test, X_train, X_test)


# ## Dummy-test

# In[ ]:


# dummy = DummyClassifier(strategy = 'most_frequent')
# dummy.fit(X_train, y_train)
# dummy.score(X_test, y_test)


# In[ ]:


# dummy_report = classification_report(y_test, dummy.predict(X_test), target_names = ['Not in Labor', 'In Labor']
# print(dummy_report)


# In[ ]:


# lr = LogisticRegression()
# grid = GridSearchCV(estimator=lr,\
#                    param_grid = { \
#                                 'C' : np.arange(0.05, 1.0, .05),\
#                                 'penalty' : ['l2'],\
#                                 'max_iter' : np.arange(500, 5000, 500)},
#                    verbose = 2)
# grid.fit(X_train, y_train)


# In[ ]:


# print(classification_report(y_test, grid.predict(X_test), target_names=['Not in Labor', 'In Labor']))
# print(confusion_matrix(y_test, grid.predict(X_test)))


# **IMPORTANT NOTE:** Logistic Regression does *no* better than guessing the most frequent.

# ## RANDOM FOREST

# In[ ]:


# rfc = ensemble.RandomForestClassifier()
# grid = GridSearchCV(estimator = rfc,
#                          param_grid={\
#                                     'max_depth' : [1, 2, 3],\
#                                     'criterion':['gini', 'entropy'],\
#                                     'min_samples_split' : np.arange(0.05,1.0, 0.05),\
#                                              },
#                    verbose=2)
# grid.fit(X_train, y_train)


# In[ ]:


# print(classification_report(y_test, grid.predict(X_test), target_names=['Not in Labor', 'In Labor']))


# **IMPORTANT NOTE** Random Forest doest *no* better than guessing the most frequent

# In[ ]:


# clf = ensemble.GradientBoostingClassifier()
# rand = RandomizedSearchCV(estimator=clf,\
#                    param_distributions = { \
#                                 'n_estimators' : np.arange(500, 1000, 250),\
#                                 'max_depth' : np.arange(1,3),\
#                                 'learning_rate' : np.arange(0.1, .90, 0.1)})
# rand.fit(X_train, y_train)
# print(classification_report(y_test, rand.predict(X_test), target_names=['Not in Labor', 'In Labor']))


# Gradient Boosting does tremendously better at predicting not in the labor force, and thus is the best model of the bunch. 

# # FURTHER CONSIDERATIONS

# In addition to the comments throughout this notebook better analysis would come from:  
# 1. Parsing out the 1-48, 1-43, 1-42, 1-9 columns and making them into rows by adding a column for month. The index could then be Person, Month for the data frame. 
# 2. Using ffill to patch up a lot of the NA's that are either dropped or ignored in this notebook.
# 3. Running the models with all the features (but not using GridSearch/RandomizedSearch), then doing some basic feature reduction (PCA, etc.)
# 4. Reconsidering the structure of the categorical data TREATLEV, POVLEV.

# In[ ]:


#gary_df['NOTINFR'] = gary_df['EMPINT'].str.contains('02')
#gary_df['NOTINFR'] = gary_df['NOTINFR'].astype(int)
#gary_df['EMPGAIN'] = gary_df['EMPINT'].str.contains('(00)(01)', regex=True)


# In[ ]:


#gary_df['EMPLOSS'] = gary_df['EMPINT'].str.contains('(01)(00)', regex=True)


# In[ ]:


#gary_df['EMPGAIN'] = gary_df.EMPGAIN.astype(int)


# In[ ]:


#gary_df['EMPLOSS'] = gary_df.EMPLOSS.astype(int)


# In[ ]:


#columns_for_later = ['EMPLOSS', 'EMPGAIN']
#gary_df.drop(columns_for_later, axis=1, inplace=True)


# In[ ]:


#gary_df['EMP'] = gary_df['EMPINT'].str.contains('01')
#gary_df['EMP'] = gary_df.EMP.astype(int)

