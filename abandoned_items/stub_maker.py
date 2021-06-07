def chunkstring(string, length):
    return [string[0 + i:length + i] for i in range(0, len(string), length)]


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
            df[column] = df[column].apply(chunkstring, args=[leng])
        stub_dict[length] = stub_cols
    return stub_dict, col_dict
