import configparser
import sys,os
from df_maker import df_maker


config = configparser.ConfigParser()
config.read('config.ini')
data = config.items('GARY_IN')
per_file, fam_file, per_var, fam_var, per_pos, fam_pos = [x[1] for x in data]

fam_var = fam_var.split(",")
per_pos, fam_pos = [x for x in tuple(map(eval, per_pos.split('\n')))], [x for x in tuple(map(eval, fam_pos.split("\n")))]
df = df_maker(per_file, fam_file, per_var, fam_var, per_pos, fam_pos)
print(df)
