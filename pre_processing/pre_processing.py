import configparser
import logging
import os
from itertools import repeat
import pandas as pd
from sqlalchemy import create_engine
from ast import literal_eval
from pathlib import Path
logging.basicConfig(filename='../nit.log', level=logging.DEBUG)


def general_df_maker(per_file, fam_file, per_vars, fam_vars, per_pos, fam_pos):
    os.chdir('../')
    fam_df = pd.read_fwf(fam_file, colspecs=fam_pos, header=None, names=fam_vars, dtype=str)
    per_df = pd.read_fwf(per_file, colspecs=per_pos, header=None, names=per_vars, dtype=str)
    return per_df.set_index("FAMNUM").join(fam_df.set_index("FAMNUM"), how="left")


def gary_maker():
    """This function creates the dataframe from Gary, Indiana
    Returns: pandas DataFrame"""
    logging.info("Beginning gary_df creation")
    config = configparser.ConfigParser()  # create configparser
    config.read('pre_processing_config.ini')
    data = config.items('GARY_IN')  # get gary's information
    per_file, fam_file, per_var, fam_var, per_pos, fam_pos = [x[1] for x in
                                                              data]
    # get variable names and relative positions from the gary file
    fam_var = fam_var.split(",")  # make it a list
    per_var = per_var.split(",\n")  # make it a list
    per_pos, fam_pos = [x for x in tuple(map(eval, per_pos.split('\n')))], [x for x in
                                                                            tuple(map(eval, fam_pos.split(
                                                                                "\n")))]  # positions must be tuples
    df = general_df_maker(per_file, fam_file, per_var, fam_var, per_pos, fam_pos)  # make the dataframe
    logging.info("Successfully created gary_df")
    return df


def chunkstring(string, length=None):
    try:
        return [string[0 + i:length + i] for i in range(0, len(string), length)]
    except ValueError:
        print(string, length)


def chunkify(df, length):
    return df.applymap(lambda x: chunkstring(x, (int(round(len(x) / length))))).astype(str)


def sql_writer(df, table_name):
    engine = create_engine('sqlite:///nit.db', echo=False)
    data_base_df = df.astype(str)
    with engine.begin() as con:
        data_base_df.to_sql(f'{table_name}', con=con, if_exists='replace')

def period_maker(df, length):
    periods = [list(range(0, length)) for _ in df.index.tolist()]
    df['PERIOD'] = periods
    return df['PERIOD'].explode()

def exploder(df, list_of_lengths):
    df_copy = df.copy().set_index('PERNUM').astype(dtype='str', copy=True).drop("JOBS0-42",
                                                               axis=1)  # TODO: figure out why JOBS0-42 is like this
    for length in list_of_lengths:
        exploded_periods = period_maker(df_copy, length)
        length_cols = [col for col in df_copy if "1-" + str(length) in col]
        length_df = df_copy.loc[:, length_cols]
        chunked_df = chunkify(length_df, length)
        exploded_list = []
        #exploded_list.append(chunked_df['PERIOD'].explode().reset_index().set_index(['PERNUM', 'PERIOD']))
        for col in chunked_df.columns:
            if col == 'PERIOD':
                break
            chunked_df[col] = chunked_df[col].apply(literal_eval)
            exploded_list.append(chunked_df[col].explode().to_frame().join(exploded_periods).reset_index().set_index(['PERNUM', 'PERIOD']))
        return pd.DataFrame(exploded_list)
        #TODO: break this up into a simple chain of commands


def main():
    logging.info('BEGINNING PRE_PROCESSING'.center(84, '='))
    df = exploder(gary_maker(), [48, 42, 16, 9])
    sql_writer(df, 'gary_exploded')
    # TODO: create merged table (using SQL or pd.Merge?) containing all the results
    # TODO: break this into sequence of handlers
    #TODO: look up tabulizer for R//tabula for Python

if __name__ == "__main__":
    main()
