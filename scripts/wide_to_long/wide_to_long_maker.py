import pandas as pd
def chunkstring(string, length):
    return [string[0+i:length+i] for i in range(0, len(string), length)]
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
gary_df = pd.read_csv('../../data/raw/raw_gary_df.csv')
gary_df = gary_df.astype(str)
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
gary_df.drop(wide_cols,axis=1, inplace=True)
stubs48 = [x[:-1] for x in stubs48_split]
stubs42 = [x[:-1] for x in stubs42_split]
stubs9 = [x[:-1] for x in stubs9_split]
stubs16 = [x[:-1] for x in stubs16_split]
stubs5 = [x[:-1] for x in stubs5_split]
stubs = [stubs48, stubs42, stubs9, stubs16, stubs5]
id_list = list(id_cols)
long48 = stubs_sorter(gary_df, stubs48)
long42 = stubs_sorter(gary_df, stubs42)
long16 = stubs_sorter(gary_df, stubs16)
long9 = stubs_sorter(gary_df, stubs9)
long5 = stubs_sorter(gary_df, stubs5)
longs = [long48, long42, long16, long9, long5]
