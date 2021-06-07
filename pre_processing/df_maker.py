import configparser
import os

import pandas as pd


def general_df_maker(per_file, fam_file, per_vars, fam_vars, per_pos, fam_pos):
    os.chdir('../')
    fam_df = pd.read_fwf(fam_file, colspecs=fam_pos, header=None, names=fam_vars, dtype=str)
    per_df = pd.read_fwf(per_file, colspecs=per_pos, header=None, names=per_vars, dtype=str)
    print(fam_df.columns, per_df.columns)
    return per_df.set_index("FAMNUM").join(fam_df.set_index("FAMNUM"), how="left")


def gary_maker():
    config = configparser.ConfigParser()
    config.read('config.ini')
    data = config.items('GARY_IN')
    per_file, fam_file, per_var, fam_var, per_pos, fam_pos = [x[1] for x in data]
    fam_var = fam_var.split(",")
    per_pos, fam_pos = [x for x in tuple(map(eval, per_pos.split('\n')))], [x for x in
                                                                            tuple(map(eval, fam_pos.split("\n")))]
    df = general_df_maker(per_file, fam_file, per_var.split(',\n'), fam_var, per_pos, fam_pos)
    print(df)
    return df
