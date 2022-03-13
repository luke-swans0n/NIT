import logging
from pathlib import Path
import pandas as pd
import numpy as np
import psycopg2

import sqlalchemy
log_path = Path("../nit.log").resolve()
logging.basicConfig(filename=log_path, level=logging.DEBUG)


def gary_maker():
    """Prepares the variables for Gary, IN."""
    logging.info("starting gary_maker()")
    perfile = Path("../data/raw/ca033001.dat").resolve()
    famfile = Path("../data/raw/ca033002.dat").resolve()
    pervars= [('FAMNUM', (0, 4)), ('PERNUM', (4, 10)), ('STATUS1-48', (10, 106)),
                    ('MOPRES1-48', (106, 154)), ('MRST1-48', (154, 250)), ('RELCODE1-48', (250, 346)),
                    ('DOB', (346, 350)), ('SEX', (349, 350)), ('ENRLDATE', (351, 356)),
                    ('ATTDATE', (356, 361)), ('DENRLDAT', (361, 366)), ('GRADE71', (366, 368)),
                    ('SCHTYP71', (368, 370)), ('GRADE72', (370, 372)), ('SCHTYP72', (372, 374)),
                    ('GRADE73', (374, 376)), ('SCHTYP73', (376, 378)), ('EVEREMP', (379, 381)),
                    ('FAMBUS', (381, 383)), ('YRSTWRK', (383, 385)), ('YRFTWRK', (385, 387)),
                    ('JOBTOTAL', (387, 389)), ('JOBS5YRS', (389, 391)), ('JOBS3YRS', (391, 393)),
                    ('JOBS1YR', (393, 395)), ('INCOME69', (395, 400)), ('EMPLOYED', (400, 402)),
                    ('LABRSTAT', (402, 404)), ('MONTHS', (404, 407)), ('INDUSTRY', (407, 410)),
                    ('OCCUPA', (410, 413)), ('HRSVARY', (413, 415)), ('SEASON', (415, 417)),
                    ('RCNTHRS', (417, 420)), ('RCNTOT', (420, 422)), ('RCNTWAGR', (422, 426)),
                    ('RCNTOTR', (426, 430)), ('RCNTPAY', (430, 436)), ('NRMLHRS', (436, 439)),
                    ('NRMLOT', (439, 441)), ('NRMLWAGR', (441, 445)), ('NRMLOTR', (445, 449)),
                    ('NRMLPAY', (449, 455)), ('DAYHRSR', (455, 458)), ('DAYRATER', (458, 462)),
                    ('DAYPAYR', (461, 468)), ('DAYHRSN', (468, 471)), ('DAYRATEN', (471, 475)),
                    ('DAYPAYN', (475, 481)), ('MOSNOWRK', (481, 483)), ('PLANWORK', (483, 485)),
                    ('SSI1-48', (499, 691)), ('TTI1-48', (691, 883)), ('SS1-48', (883, 1075)),
                    ('VA1-48', (1077, 1267)), ('MISINC1-48', (1267, 1459)), ('OTHINC1-48', (1459, 1651)),
                    ('JOBSINC1-48', (1651, 1843)), ('DAYINC1-48', (1843, 2035)), ('OJINC1-48', (2035, 2227)),
                    ('UEMBEN1-48', (2227, 2419)), ('STRKWC1-48', (2419, 2611)), ('EMPSTAT1-9', (2611, 2629)),
                    ('TYPWRKR1-9', (2629, 2647)), ('WYNOWRK1-9', (2647, 2665)), ('HRSWEEK1-9', (2665, 2692)),
                    ('OTHRSWK1-9', (2692, 2719)), ('HRSREG1-9', (2719, 2746)), ('OTHREG1-9', (2746, 2773)),
                    ('DSABLED1-9', (2773, 2791)), ('DISLMIT1-9', (2791, 2809)), ('TYPWRK1-48', (2809, 2905)),
                    ('PCTEMP1-48', (2905, 3097)), ('PCTWRK1-48', (3097, 3289)), ('REASON1-48', (3289, 3385)),
                    ('PCNTLF1-48', (3385, 3577)), ('PCTUMP1-48', (3577, 3769)), ('EMPSTA1-48', (3769, 3865)),
                    ('DISABL1-48', (3865, 3961)), ('NUMJBS1-48', (3961, 4057)), ('EXPER1-48', (4057, 4201)),
                    ('INDUS1-48', (4201, 4345)), ('OCCUP1-48', (4345, 4537)), ('WKRLNG1-48', (4537, 4729)),
                    ('HOURS1-48', (4729, 4921)), ('HRCHNG1-48', (4921, 5017)), ('OTHRS1-48', (5017, 5209)),
                    ('WGRATE1-48', (5209, 5401)), ('WGCHNG1-48', (5401, 5497)), ('SINWGS69-73', (8414, 8444)),
                    ('SJTWGS69-73', (8444, 8474)), ('WAGES70', (8474, 8479)), ('QTRWRK70', (8479, 8481)),
                    ('WGSECON', (8481, 8485)), ('WGSART1-16', (8485, 8549)), ('UNEMP1-48', (8549, 8741)),
                    ('OTRATE1-48', (5497, 5593)), ('GWAGES0-42', (5593, 5765)), ('FTXWTH0-42', (5765, 5937)),
                    ('STXWTH0-42', (5937, 6109)), ('FICA0-42', (6109, 6281)), ('JOBS0-42', (6281, 6496)),
                    ('HRSWRK0-42', (6496, 6582)), ('REGHRS0-42', (6582, 6754)), ('OVRTME0-42', (6926, 7098)),
                    ('SPECL0-42', (7098, 7270)), ('SPCLCD0-42', (7270, 7356)), ('AFDC1970', (7356, 7360)),
                    ('AFDCM070', (7360, 7362)), ('AFDCBASE', (7362, 7366)), ('AFDC1-48', (7366, 7558)),
                    ('AFDCEL1-48', (7558, 7750)), ('SSI1970', (7750, 7754)), ('SSIMOS70', (7754, 7756)),
                    ('SSIBASE', (7756, 7760))]
    famvars = [("FAMNUM", (0, 4)), ("POVLEV", (6, 7)), ("TREATLEV", (9, 10))]
    return pervars, famvars, perfile, famfile
def create_dataframe(personfile, familyfile, personvariables, familyvariables):
    pernames = [x[0] for x in personvariables]
    perpositions = [x[1] for x in personvariables]
    famnames = [x[0] for x in familyvariables]
    fampositions = [x[1] for x in familyvariables]
    fam_df = pd.read_fwf(familyfile, colspecs=fampositions, header=None, names=famnames, dtype=str)
    per_df = pd.read_fwf(personfile, colspecs=perpositions, header=None, names=pernames, dtype=str)
    return per_df.set_index("FAMNUM").join(fam_df.set_index("FAMNUM"), how="left")
def stringsplitter(string, period):
    size = int(len(string)/int(period))
    if size==0:
        return
    result = [string[x:x+size] for x in range(0, len(string), size)]
    return result
if __name__ == "__main__":
    pervars, famvars, perfile, famfile = gary_maker()
    gary_df = create_dataframe(perfile, famfile, pervars, famvars)
    #TODO: determine cause of JOBS-42 being NaN?
    gary_df.drop(columns='JOBS0-42', axis=1, inplace=True)
    periodics = {"period48": [gary_df[[column for column in gary_df.columns if "1-48" in column]], 48],
                     "period42": [gary_df[[column for column in gary_df.columns if "0-42" in column]],42],
                     "period16": [gary_df[[column for column in gary_df.columns if "1-16" in column]],16],
                     "period9": [gary_df[[column for column in gary_df.columns if "1-9" in column]],9]}
    engine = sqlalchemy.create_engine("postgresql://posgres:Pyth4g0r4$@localhost:5432/nit")
    for df in periodics.values():
        df[0] = df[0].applymap(lambda string: stringsplitter(string, df[1]))
        df.to_sql(df[1], engine)

    print('done.')
     #   value.to_sql(f"{key}", engine)
    #engine.dispose()
