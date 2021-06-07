from itertools import cycle

from chunkstring import chunkstring as chunk
from df_maker import gary_maker

# nit = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     user = "the_administrator",
#     password = 'negative_income'
# )
#
# mycursor = nit.cursor()


# cur.execute('''CREATE TABLE [IF NOT EXISTS] gary_demographics
# (pernum TEXT PRIMARY KEY,
# famnum TEXT NOT NULL UNIQUE,
# def write_to_sql(name, df):
#     try:
#         df.to_sql(name, con=nit, chunksize=1000)
#         print('success!')
#     except ValueError:
#         print("table already exists.")
#

def exploder(df, list_of_lengths):
    test_dict = {}
    for length in list_of_lengths:
        test_df = df.copy().set_index('PERNUM').applymap(str).drop("JOBS0-42", axis=1)
        no_operation_columns = [col for col in test_df.columns if "-" not in col]
        periods = [list(range(0, length))]* len(test_df)
        test_dict[length] = test_df.loc[:, [col for col in test_df if "1-"+str(length) in col]].applymap(lambda x: chunk(x, int(len(x)/length)))
        test_dict[length]['PERIOD'] = periods
        test_dict[length] = test_dict[length].reset_index(drop=True).apply(lambda x: x.explode())
        return df




        # write_to_sql("test", frame)
    # final_frame = list_of_frames[0].join(list_of_frames, how='outer')
    # final_frame.reset_index(level='PERIOD', inplace=True)
    # write_to_sql('demographics'.test_df[no_operation_columns])


def main():
    gary = exploder(gary_maker(), [48, 42, 16, 9])
    print(gary)

if __name__ == "__main__":
    main()
# gary_df = pd.read_csv('raw_gary_df.csv', dtype=str)
# gary_df.drop('Unnamed: 0', axis=1, inplace=True)
# gary_df.dropna(inplace=True)
#
# no_operation_columns = gary_df.loc[:, [col for col in gary_df.columns if "-" not in col]]
# lengths = ['-48', '-42', '-9', '-16', '-73']
#
# stubs, cols = stub.stub_maker(gary_df, lengths)
#
# test_dict = {}
#
# tiles = list(np.arange(1, 49))*5326
# test_df = gary_df.copy()
# test_dict['-48'] = test_df.loc[:, [col for col in test_df if '48' in col]].apply(lambda x: x.explode())
# test_dict['-48']['PERIOD'] = tiles
#
# tiles = list(np.arange(0, 43))*5326
# test_df = gary_df.copy()
# test_dict['-42'] = test_df.loc[:, [col for col in test_df if '42' in col]].apply(lambda x: x.explode())
# test_dict['-42']['PERIOD'] = tiles
#
# tiles = list(np.arange(8, 49, 5))*5326
# test_df = gary_df.copy()
# test_dict['-9'] = test_df.loc[:, [col for col in test_df if '-9' in col]].apply(lambda x: x.explode())
# test_dict['-9']['PERIOD'] = tiles
#
# tiles = list(np.arange(3, 49, 3))*5326
# test_df = gary_df.copy()
# test_dict['-16'] = test_df.loc[:, [col for col in test_df if '16' in col]].apply(lambda x: x.explode())
# test_dict['-16']['PERIOD'] = tiles
#
# tiles = list(np.arange(8, 49,10 ))*5326
# test_df = gary_df.copy()
# test_dict['-73'] = test_df.loc[:, [col for col in test_df if '69-73' in col]].apply(lambda x: x.explode())
# test_dict['-73']['PERIOD'] = tiles
#
