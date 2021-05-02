import pandas as pd
import numpy as np
def df_maker(per_file, fam_file, per_vars, fam_vars, per_pos, fam_pos):

    fam_dict = dict(zip(fam_vars, fam_pos))
    df = pd.read_fwf(fam_file, colspecs=fam_pos, header=None, names=fam_vars)
    return df


