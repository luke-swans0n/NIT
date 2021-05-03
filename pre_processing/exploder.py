import pandas as pd
import numpy as np
import gary_df_maker
import stub_maker as stub

gary_df = pd.read_csv('raw_gary_df.csv', dtype=str)
gary_df.drop('Unnamed: 0', axis=1, inplace=True)
gary_df.dropna(inplace=True)

no_operation_columns = gary_df.loc[:, [col for col in gary_df.columns if "-" not in col]]
lengths = ['-48', '-42', '-9', '-16', '-73']

stubs, cols = stub.stub_maker(gary_df, lengths)

test_dict = {}

tiles = list(np.arange(1, 49))*5326
test_df = gary_df.copy()
test_dict['-48'] = test_df.loc[:, [col for col in test_df if '48' in col]].apply(lambda x: x.explode())
test_dict['-48']['PERIOD'] = tiles

tiles = list(np.arange(0, 43))*5326
test_df = gary_df.copy()
test_dict['-42'] = test_df.loc[:, [col for col in test_df if '42' in col]].apply(lambda x: x.explode())
test_dict['-42']['PERIOD'] = tiles

tiles = list(np.arange(8, 49, 5))*5326
test_df = gary_df.copy()
test_dict['-9'] = test_df.loc[:, [col for col in test_df if '-9' in col]].apply(lambda x: x.explode())
test_dict['-9']['PERIOD'] = tiles

tiles = list(np.arange(3, 49, 3))*5326
test_df = gary_df.copy()
test_dict['-16'] = test_df.loc[:, [col for col in test_df if '16' in col]].apply(lambda x: x.explode())
test_dict['-16']['PERIOD'] = tiles

tiles = list(np.arange(8, 49,10 ))*5326
test_df = gary_df.copy()
test_dict['-73'] = test_df.loc[:, [col for col in test_df if '69-73' in col]].apply(lambda x: x.explode())
test_dict['-73']['PERIOD'] = tiles

list_of_frames = [test_dict['-42'].reset_index().set_index(['index', 'PERIOD']), 
                  test_dict['-9'].reset_index().set_index(['index', 'PERIOD']),
                  test_dict['-16'].reset_index().set_index(['index', 'PERIOD']),
                  test_dict['-73'].reset_index().set_index(['index', 'PERIOD'])]
final_frame = test_dict['-48'].reset_index().set_index(['index', 'PERIOD']).join(list_of_frames, how='outer')
final_frame.reset_index(level='PERIOD', inplace=True)
final_frame = final_frame.join(no_operation_columns, how='outer')
final_frame.to_csv("gary_exploded_script.csv")
