#!/usr/bin/env python
# coding: utf-8

# # CAPSTONE TWO: NEGATIVE INCOME TAX EXPERIMENTS

# ## IMPORTS
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# ## THE PERSON FILE

# We need to read in the person file, which contains the target data as well as other data, and merge it with the family file which contains the treatment level and the poverty level.

# In[2]:


# GARY_FILE_PERSON_RECORD'
GARY_FILE_PERSON_RECORD_PATH = "../data/raw/ca033001.dat"
var_list = [
    "FAMNUM",
    "PERNUM",
    "STATUS1-48",
    "MOPRES1-48",
    "MRST1-48",
    "RELCODE1-48",
    "DOB",
    "SEX",
    "ENRLDATE",
    "ATTDATE",
    "DENRLDAT",
    "GRADE71",
    "SCHTYP71",
    "GRADE72",
    "SCHTYP72",
    "GRADE73",
    "SCHTYP73",
    "EVEREMP",
    "FAMBUS",
    "YRSTWRK",
    "YRFTWRK",
    "JOBTOTAL",
    "JOBS5YRS",
    "JOBS3YRS",
    "JOBS1YR",
    "INCOME69",
    "EMPLOYED",
    "LABRSTAT",
    "MONTHS",
    "INDUSTRY",
    "OCCUPA",
    "HRSVARY",
    "SEASON",
    "RCNTHRS",
    "RCNTOT",
    "RCNTWAGR",
    "RCNTOTR",
    "RCNTPAY",
    "NRMLHRS",
    "NRMLOT",
    "NRMLWAGR",
    "NRMLOTR",
    "NRMLPAY",
    "DAYHRSR",
    "DAYRATER",
    "DAYPAYR",
    "DAYHRSN",
    "DAYRATEN",
    "DAYPAYN",
    "MOSNOWRK",
    "PLANWORK",
    "SSI1-48",
    "TTI1-48",
    "SS1-48",
    "VA1-48",
    "MISINC1-48",
    "OTHINC1-48",
    "JOBSINC1-48",
    "DAYINC1-48",
    "OJINC1-48",
    "UEMBEN1-48",
    "STRKWC1-48",
    "EMPSTAT1-9",
    "TYPWRKR1-9",
    "WYNOWRK1-9",
    "HRSWEEK1-9",
    "OTHRSWK1-9",
    "HRSREG1-9",
    "OTHREG1-9",
    "DSABLED1-9",
    "DISLMIT1-9",
    "TYPWRK1-48",
    "PCTEMP1-48",
    "PCTWRK1-48",
    "REASON1-48",
    "PCNTLF1-48",
    "PCTUMP1-48",
    "EMPSTA1-48",
    "DISABL1-48",
    "NUMJBS1-48",
    "EXPER1-48",
    "INDUS1-48",
    "OCCUP1-48",
    "WKRLNG1-48",
    "HOURS1-48",
    "HRCHNG1-48",
    "OTHRS1-48",
    "WGRATE1-48",
    "WGCHNG1-48",
    "SINWGS69-73",
    "SJTWGS69-73",
    "WAGES70",
    "QTRWRK70",
    "WGSECON",
    "WGSART1-16",
    "UNEMP1-48",
    "OTRATE1-48",
    "GWAGES0-42",
    "FTXWTH0-42",
    "STXWTH0-42",
    "FICA0-42",
    "JOBS0-42",
    "HRSWRK0-42",
    "REGHRS0-42",
    "OVRTME0-42",
    "SPECL0-42",
    "SPCLCD0-42",
    "AFDC1970",
    "AFDCM070",
    "AFDCBASE",
    "AFDC1-48",
    "AFDCEL1-48",
    "SSI1970",
    "SSIMOS70",
    "SSIBASE",
]
data_set = []
with open(GARY_FILE_PERSON_RECORD_PATH) as file:
    for line in file:
        data = [
            line[1 - 1 : 4],
            line[5 - 1 : 10],
            line[11 - 1 : 106],
            line[107 - 1 : 154],
            line[155 - 1 : 250],
            line[251 - 1 : 346],
            line[347 - 1 : 350],
            line[350],
            line[352 - 1 : 356],
            line[357 - 1 : 361],
            line[362 - 1 : 366],
            line[367 - 1 : 368],
            line[369 - 1 : 370],
            line[371 - 1 : 372],
            line[373 - 1 : 374],
            line[375 - 1 : 376],
            line[377 - 1 : 378],
            line[380 - 1 : 381],
            line[382 - 1 : 383],
            line[384 - 1 : 385],
            line[386 - 1 : 387],
            line[388 - 1 : 389],
            line[390 - 1 : 391],
            line[392 - 1 : 393],
            line[394 - 1 : 395],
            line[396 - 1 : 400],
            line[401 - 1 : 402],
            line[403 - 1 : 404],
            line[405 - 1 : 407],
            line[408 - 1 : 410],
            line[411 - 1 : 413],
            line[414 - 1 : 415],
            line[416 - 1 : 417],
            line[418 - 1 : 420],
            line[421 - 1 : 422],
            line[423 - 1 : 426],
            line[427 - 1 : 430],
            line[431 - 1 : 436],
            line[437 - 1 : 439],
            line[440 - 1 : 441],
            line[442 - 1 : 445],
            line[446 - 1 : 449],
            line[449:455],
            line[456 - 1 : 458],
            line[459 - 1 : 462],
            line[463 - 1 : 468],
            line[469 - 1 : 471],
            line[472 - 1 : 475],
            line[476 - 1 : 481],
            line[482 - 1 : 483],
            line[484 - 1 : 485],
            line[500 - 1 : 691],
            line[692 - 1 : 883],
            line[884 - 1 : 1075],
            line[1076 - 1 : 1267],
            line[1268 - 1 : 1459],
            line[1460 - 1 : 1651],
            line[1652 - 1 : 1843],
            line[1844 - 1 : 2035],
            line[2036 - 1 : 2227],
            line[2228 - 1 : 2419],
            line[2420 - 1 : 2611],
            line[2612 - 1 : 2629],
            line[2630 - 1 : 2647],
            line[2648 - 1 : 2665],
            line[2666 - 1 : 2692],
            line[2693 - 1 : 2719],
            line[2720 - 1 : 2746],
            line[2747 - 1 : 2773],
            line[2774 - 1 : 2791],
            line[2792 - 1 : 2809],
            line[2810 - 1 : 2905],
            line[2906 - 1 : 3097],
            line[3098 - 1 : 3289],
            line[3290 - 1 : 3385],
            line[3386 - 1 : 3577],
            line[3578 - 1 : 3769],
            line[3770 - 1 : 3865],
            line[3866 - 1 : 3961],
            line[3962 - 1 : 4057],
            line[4058 - 1 : 4201],
            line[4202 - 1 : 4345],
            line[4346 - 1 : 4537],
            line[4538 - 1 : 4729],
            line[4730 - 1 : 4921],
            line[4922 - 1 : 5017],
            line[5018 - 1 : 5209],
            line[5210 - 1 : 5401],
            line[5402 - 1 : 5497],
            line[8415 - 1 : 8444],
            line[8445 - 1 : 8474],
            line[8475 - 1 : 8479],
            line[8480 - 1 : 8481],
            line[8482 - 1 : 8485],
            line[8486 - 1 : 8549],
            line[8550 - 1 : 8741],
            line[5498 - 1 : 5593],
            line[5594 - 1 : 5765],
            line[5766 - 1 : 5937],
            line[5938 - 1 : 6109],
            line[6110 - 1 : 6281],
            line[6282 - 1 : 6496],
            line[6497 - 1 : 6582],
            line[6583 - 1 : 6754],
            line[6927 - 1 : 7098],
            line[7099 - 1 : 7270],
            line[7271 - 1 : 7356],
            line[7357 - 1 : 7360],
            line[7361 - 1 : 7362],
            line[7363 - 1 : 7366],
            line[7367 - 1 : 7558],
            line[7559 - 1 : 7750],
            line[7751 - 1 : 7754],
            line[7755 - 1 : 7756],
            line[7757 - 1 : 7760],
        ]
        data_set.append(data)
# In[3]:
person_df = pd.DataFrame(np.array(data_set), columns=var_list)
# ## THE FAMILY FILE
# In[4]:
var_list = ["FAMNUM", "POVLEV", "TREATLEV"]
data_set = []
with open("../data/raw/ca033002.dat") as file:
    for line in file:
        data = [line[0:4], line[6], line[8]]
        data_set.append(data)
# In[5]:
fam_df = pd.DataFrame(np.array(data_set), columns=var_list)
# ## MERGING
# We use an outer merge here to collect all of the entries from both tables.
# In[6]:
fam_df.FAMNUM.astype(int)
person_df.FAMNUM.astype(int)
gary_df = person_df.merge(fam_df, on="FAMNUM", how="outer")
gary_df.to_csv(r"..\data\raw\raw_gary_df")
# ## DATA CLEANING
# In[7]:
# gary_df.dropna(inplace=True)


# ### WIDE DATA -> LONG DATA

# In[8]:
"""

wide_cols = [col for col in gary_df.columns if '-' in col]
stubs48_split = []
stubs42_split = []
stubs9_split = []
stubs16_split = []
stubs5_split = []
id_cols = gary_df.drop(wide_cols, axis =1).columns
cols_48 = [col for col in gary_df.columns if '-48' in col]
cols_42 = [col for col in gary_df.columns if '-42' in col]
cols_9 = [col for col in gary_df.columns if '-9' in col]
cols_16 = [col for col in gary_df.columns if '-16' in col]
cols_5 = [col for col in gary_df.columns if '-5' in col]


# In[9]:


#def col_chunkify():
    #add code from cell below


# In[10]:


def chunkstring(string, length):
    return [string[0+i:length+i] for i in range(0, len(string), length)]
for column in wide_cols:
    if '-48' in column:
        stubs48_split.append(column.split('-')[0])
        leng = int(gary_df[column].str.len().unique() /48)
        gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
        for i in range(48):
            gary_df[column[:-4] + str(i+1)] = gary_df[column].apply(lambda x: x[i])
    if '-42' in column:
        stubs42_split.append(column.split('-')[0])
        leng = int(gary_df[column].str.len().unique() /42)
        gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
        for i in range(42):
            gary_df[column[:-4] + str(i+1)] = gary_df[column].apply(lambda x: x[i])
    if '-9' in column:
        stubs9_split.append(column.split('-')[0])
        leng = int(gary_df[column].str.len().unique() /9)
        gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
        for i in range(9):
            gary_df[column[:-3] + str(i+1)] = gary_df[column].apply(lambda x: x[i])
    if '-16' in column:
        stubs16_split.append(column.split('-')[0])
        leng = int(gary_df[column].str.len().unique() /16)
        gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
        for i in range(16):
            gary_df[column[:-3] + str(i+1)] = gary_df[column].apply(lambda x: x[i])
    if '-73' in column:
        stubs5_split.append(column.split('-')[0])
        leng = int(gary_df[column].str.len().unique() /5)
        gary_df[column] = gary_df[column].apply(chunkstring, args=[leng])
        for i in range(5):
            gary_df[column[:-3] + str(i+1)] = gary_df[column].apply(lambda x: x[i])


# In[11]:


gary_df.drop(wide_cols,axis=1, inplace=True)


# In[12]:


stubs48 = [x[:-1] for x in stubs48_split]
stubs42 = [x[:-1] for x in stubs42_split]
stubs9 = [x[:-1] for x in stubs9_split]
stubs16 = [x[:-1] for x in stubs16_split]
stubs5 = [x[:-1] for x in stubs5_split]
stubs = [stubs48, stubs42, stubs9, stubs16, stubs5]
id_list = list(id_cols)


# In[13]:


def stubs_sorter(df, stubs_list):
    cols_list = []
    for stub in stubs_list:
        lengths = set([len(stub)+1, len(stub)+2])
        cols_list += [col for col in df.columns if stub in col and len(col) in lengths]
    if any('48' in col for col in cols_list):
        special_case = ['EMPSTAT1', 'TYPWRKR7', 'TYPWRKR3', 'TYPWRKR8', 'EMPSTAT7', 'EMPSTAT9',
           'TYPWRKR1', 'EMPSTAT8', 'TYPWRKR6', 'TYPWRKR9', 'EMPSTAT2', 'EMPSTAT4',
           'TYPWRKR2', 'EMPSTAT3', 'TYPWRKR5', 'EMPSTAT6', 'EMPSTAT5', 'TYPWRKR4']
        for col in special_case:
            cols_list.remove(col)
    #cols_list = [col for col in gary_df.columns if stubs48[0] in col]
    cols_list.append('PERNUM')
    #gary_df[cols_list]
    #gary_df['id'] = gary_df.index
    df_long = pd.wide_to_long(gary_df[cols_list], stubnames=stubs_list, i ='PERNUM', j="period")
    return df_long
# In[14]:
long48 = stubs_sorter(gary_df, stubs48)
long42 = stubs_sorter(gary_df, stubs42)
long16 = stubs_sorter(gary_df, stubs16)
long9 = stubs_sorter(gary_df, stubs9)
long5 = stubs_sorter(gary_df, stubs5)
longs = [long48, long42, long16, long9, long5]
long5
# In[15]:
for df in longs:
    df.reset_index(inplace=True)
    df.drop_duplicates(inplace=True)
# In[16]:
map9 = {1 : 1, 2 : 14, 3 : 18, 4 : 22, 5 : 26, 6 : 31, 7 : 35, 8 : 38, 9 : 43}
map5 = {91 : 1, 92 : 13, 93 : 25, 94 : 37, 95 : 48}
long16['period'] = long16['period']*4
long9['period'] = long9['period'].map(map9)
long5['period'] = long5['period'].map(map5)
# In[17]:
long9.sort_values(by = ['PERNUM', 'period'])
# In[18]:
long5.sort_values(by = ['PERNUM', 'period'])
# In[19]:
gary_final = pd.merge(long5, long9, on=['PERNUM', 'period'])
gary_final.head(500)
# In[20]:
gary_final.loc[gary_final['PERNUM'] =='500001']

"""
