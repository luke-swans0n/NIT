from configparser import ConfigParser

config = ConfigParser()
config['LOCATION_FLAGS'] = {
    "All": "False",
    "Gary, IN": "True",
    "TBD": "False"}
config["GARY_IN"] = {
    "gary_per_record_file": "/home/the_administrator/DATA_SCIENCE_PROJECTS/NIT/data/raw/ca033001.dat",
    "gary_fam_record_file": "/home/the_administrator/DATA_SCIENCE_PROJECTS/NIT/data/raw/ca033002.dat",
    "gary_per_var_list": """FAMNUM,
                 PERNUM,
                 STATUS1-48,
                 MOPRES1-48,
                 MRST1-48,
                 RELCODE1-48,
                 DOB,
                 SEX,
                 ENRLDATE,
                 ATTDATE,
                 DENRLDAT,
                 GRADE71,
                 SCHTYP71,
                 GRADE72,
                 SCHTYP72,
                 GRADE73,
                 SCHTYP73,
                 EVEREMP,
                 FAMBUS,
                 YRSTWRK,
                 YRFTWRK,
                 JOBTOTAL,
                 JOBS5YRS,
                 JOBS3YRS,
                 JOBS1YR,
                 INCOME69,
                 EMPLOYED,
                 LABRSTAT,
                 MONTHS,
                 INDUSTRY,
                 OCCUPA,
                 HRSVARY,
                 SEASON,
                 RCNTHRS,
                 RCNTOT,
                 RCNTWAGR,
                 RCNTOTR,
                 RCNTPAY,
                 NRMLHRS,
                 NRMLOT,
                 NRMLWAGR,
                 NRMLOTR,
                 NRMLPAY,
                 DAYHRSR,
                 DAYRATER,
                 DAYPAYR,
                 DAYHRSN,
                 DAYRATEN,
                 DAYPAYN,
                 MOSNOWRK,
                 PLANWORK,
                 SSI1-48,
                 TTI1-48,
                 SS1-48,
                 VA1-48,
                 MISINC1-48,
                 OTHINC1-48,
                 JOBSINC1-48,
                 DAYINC1-48,
                 OJINC1-48,
                 UEMBEN1-48,
                 STRKWC1-48,
                 EMPSTAT1-9,
                 TYPWRKR1-9,
                 WYNOWRK1-9,
                 HRSWEEK1-9,
                 OTHRSWK1-9,
                 HRSREG1-9,
                 OTHREG1-9,
                 DSABLED1-9,
                 DISLMIT1-9,
                 TYPWRK1-48,
                 PCTEMP1-48,
                 PCTWRK1-48,
                 REASON1-48,
                 PCNTLF1-48,
                 PCTUMP1-48,
                 EMPSTA1-48,
                 DISABL1-48,
                 NUMJBS1-48,
                 EXPER1-48,
                 INDUS1-48,
                 OCCUP1-48,
                 WKRLNG1-48,
                 HOURS1-48,
                 HRCHNG1-48,
                 OTHRS1-48,
                 WGRATE1-48,
                 WGCHNG1-48,
                 SINWGS69-73,
                 SJTWGS69-73,
                 WAGES70,
                 QTRWRK70,
                 WGSECON,
                 WGSART1-16,
                 UNEMP1-48,
                 OTRATE1-48,
                 GWAGES0-42,
                 FTXWTH0-42,
                 STXWTH0-42,
                 FICA0-42,
                 JOBS0-42,
                 HRSWRK0-42,
                 REGHRS0-42,
                 OVRTME0-42,
                 SPECL0-42,
                 SPCLCD0-42,
                 AFDC1970,
                 AFDCM070,
                 AFDCBASE,
                 AFDC1-48,
                 AFDCEL1-48,
                 SSI1970,
                 SSIMOS70,
                 SSIBASE,""",
    "gary_fam_var_list": 'FAMNUM, POVLEV, TREATLEV',
    "gary_per_pos_list": """(0, 4)
        (4, 10)
        (10, 106)
        (106, 154)
        (154, 250)
        (250, 346)
        (346, 350)
        (349, 350)
        (351, 356)
        (356, 361)
        (361, 366)
        (366, 368)
        (368, 370)
        (370, 372)
        (372, 374)
        (374, 376)
        (376, 378)
        (379, 381)
        (381, 383)
        (383, 385)
        (385, 387)
        (387, 389)
        (389, 391)
        (391, 393)
        (393, 395)
        (395, 400)
        (400, 402)
        (402, 404)
        (404, 407)
        (407, 410)
        (410, 413)
        (413, 415)
        (415, 417)
        (417, 420)
        (420, 422)
        (422, 426)
        (426, 430)
        (430, 436)
        (436, 439)
        (439, 441)
        (441, 445)
        (445, 449)
        (449, 455)
        (455, 458)
        (458, 462)
        (461, 468)
        (468, 471)
        (471, 475)
        (475, 481)
        (481, 483)
        (483, 485)
        (499, 691)
        (691, 883)
        (883, 1075)
        (1077, 1267)
        (1267, 1459)
        (1459, 1651)
        (1651, 1843)
        (1843, 2035)
        (2035, 2227)
        (2227, 2419)
        (2419, 2611)
        (2611, 2629)
        (2629, 2647)
        (2647, 2665)
        (2665, 2692)
        (2692, 2719)
        (2719, 2746)
        (2746, 2773)
        (2773, 2791)
        (2791, 2809)
        (2809, 2905)
        (2905, 3097)
        (3097, 3289)
        (3289, 3385)
        (3385, 3577)
        (3577, 3769)
        (3769, 3865)
        (3865, 3961)
        (3961, 4057)
        (4057, 4201)
        (4201, 4345)
        (4345, 4537)
        (4537, 4729)
        (4729, 4921)
        (4921, 5017)
        (5017, 5209)
        (5209, 5401)
        (5401, 5497)
        (8414, 8444)
        (8444, 8474)
        (8474, 8479)
        (8479, 8481)
        (8481, 8485)
        (8485, 8549)
        (8549, 8741)
        (5497, 5593)
        (5593, 5765)
        (5765, 5937)
        (5937, 6109)
        (6109, 6281)
        (6281, 6496)
        (6496, 6582)
        (6582, 6754)
        (6926, 7098)
        (7098, 7270)
        (7270, 7356)
        (7356, 7360)
        (7360, 7362)
        (7362, 7366)
        (7366, 7558)
        (7558, 7750)
        (7750, 7754)
        (7754, 7756)
        (7756, 7760)""",
    "gary_fam_pos_list": """(0, 4)
                         (6, 7)
                         (9, 10)"""

}
with open('pre_processing_config.ini', 'w') as configfile:
    config.write(configfile)
