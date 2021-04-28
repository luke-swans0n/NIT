from configparser import ConfigParser

config = ConfigParser()
config['LOCATION_FLAGS'] = {
    "All": "False",
    "Gary, IN": "True",
    "TBD": "False"}
config["GARY_IN"] = {
    "gary_per_record_file" : "ca033001.dat" ,
    "gary_fam_record_file" : "ca033002.dat",
    "gary_per_var_list": ["FAMNUM",
                 "PERNUM",
                 "STATUS1-48",
                 "MOPRES1-48",
                 "MRST1-48",
                 "RELCODE1-48",
                 "DOB",
                 "SEX",
                 "ENRLDATE",
                 "ATTDATE",
                 "DENRLDAT",
                 "GRADE71",
                 "SCHTYP71",
                 "GRADE72",
                 "SCHTYP72",
                 "GRADE73",
                 "SCHTYP73",
                 "EVEREMP",
                 "FAMBUS",
                 "YRSTWRK",
                 "YRFTWRK",
                 "JOBTOTAL",
                 "JOBS5YRS",
                 "JOBS3YRS",
                 "JOBS1YR",
                 "INCOME69",
                 "EMPLOYED",
                 "LABRSTAT",
                 "MONTHS",
                 "INDUSTRY",
                 "OCCUPA",
                 "HRSVARY",
                 "SEASON",
                 "RCNTHRS",
                 "RCNTOT",
                 "RCNTWAGR",
                 "RCNTOTR",
                 "RCNTPAY",
                 "NRMLHRS",
                 "NRMLOT",
                 "NRMLWAGR",
                 "NRMLOTR",
                 "NRMLPAY",
                 "DAYHRSR",
                 "DAYRATER",
                 "DAYPAYR",
                 "DAYHRSN",
                 "DAYRATEN",
                 "DAYPAYN",
                 "MOSNOWRK",
                 "PLANWORK",
                 "SSI1-48",
                 "TTI1-48",
                 "SS1-48",
                 "VA1-48",
                 "MISINC1-48",
                 "OTHINC1-48",
                 "JOBSINC1-48",
                 "DAYINC1-48",
                 "OJINC1-48",
                 "UEMBEN1-48",
                 "STRKWC1-48",
                 "EMPSTAT1-9",
                 "TYPWRKR1-9",
                 "WYNOWRK1-9",
                 "HRSWEEK1-9",
                 "OTHRSWK1-9",
                 "HRSREG1-9",
                 "OTHREG1-9",
                 "DSABLED1-9",
                 "DISLMIT1-9",
                 "TYPWRK1-48",
                 "PCTEMP1-48",
                 "PCTWRK1-48",
                 "REASON1-48",
                 "PCNTLF1-48",
                 "PCTUMP1-48",
                 "EMPSTA1-48",
                 "DISABL1-48",
                 "NUMJBS1-48",
                 "EXPER1-48",
                 "INDUS1-48",
                 "OCCUP1-48",
                 "WKRLNG1-48",
                 "HOURS1-48",
                 "HRCHNG1-48",
                 "OTHRS1-48",
                 "WGRATE1-48",
                 "WGCHNG1-48",
                 "SINWGS69-73",
                 "SJTWGS69-73",
                 "WAGES70",
                 "QTRWRK70",
                 "WGSECON",
                 "WGSART1-16",
                 "UNEMP1-48",
                 "OTRATE1-48",
                 "GWAGES0-42",
                 "FTXWTH0-42",
                 "STXWTH0-42",
                 "FICA0-42",
                 "JOBS0-42",
                 "HRSWRK0-42",
                 "REGHRS0-42",
                 "OVRTME0-42",
                 "SPECL0-42",
                 "SPCLCD0-42",
                 "AFDC1970",
                 "AFDCM070",
                 "AFDCBASE",
                 "AFDC1-48",
                 "AFDCEL1-48",
                 "SSI1970",
                 "SSIMOS70",
                 "SSIBASE", ],
    "gary_fam_var_list": ["FAMNUM", "POVLEV", "TREATLEV"],
    "gary_per_pos_list": [(1 - 1, 4),
                      (5 - 1, 10),
                      (11 - 1, 106),
                      (107 - 1, 154),
                      (155 - 1, 250),
                      (251 - 1, 346),
                      (347 - 1, 350),
                      (350, 350),
                      (352 - 1, 356),
                      (357 - 1, 361),
                      (362 - 1, 366),
                      (367 - 1, 368),
                      (369 - 1, 370),
                      (371 - 1, 372),
                      (373 - 1, 374),
                      (375 - 1, 376),
                      (377 - 1, 378),
                      (380 - 1, 381),
                      (382 - 1, 383),
                      (384 - 1, 385),
                      (386 - 1, 387),
                      (388 - 1, 389),
                      (390 - 1, 391),
                      (392 - 1, 393),
                      (394 - 1, 395),
                      (396 - 1, 400),
                      (401 - 1, 402),
                      (403 - 1, 404),
                      (405 - 1, 407),
                      (408 - 1, 410),
                      (411 - 1, 413),
                      (414 - 1, 415),
                      (416 - 1, 417),
                      (418 - 1, 420),
                      (421 - 1, 422),
                      (423 - 1, 426),
                      (427 - 1, 430),
                      (431 - 1, 436),
                      (437 - 1, 439),
                      (440 - 1, 441),
                      (442 - 1, 445),
                      (446 - 1, 449),
                      (449, 455),
                      (456 - 1, 458),
                      (459 - 1, 462),
                      (463 - 1, 468),
                      (469 - 1, 471),
                      (472 - 1, 475),
                      (476 - 1, 481),
                      (482 - 1, 483),
                      (484 - 1, 485),
                      (500 - 1, 691),
                      (692 - 1, 883),
                      (884 - 1, 1075),
                      (1076 - 1, 1267),
                      (1268 - 1, 1459),
                      (1460 - 1, 1651),
                      (1652 - 1, 1843),
                      (1844 - 1, 2035),
                      (2036 - 1, 2227),
                      (2228 - 1, 2419),
                      (2420 - 1, 2611),
                      (2612 - 1, 2629),
                      (2630 - 1, 2647),
                      (2648 - 1, 2665),
                      (2666 - 1, 2692),
                      (2693 - 1, 2719),
                      (2720 - 1, 2746),
                      (2747 - 1, 2773),
                      (2774 - 1, 2791),
                      (2792 - 1, 2809),
                      (2810 - 1, 2905),
                      (2906 - 1, 3097),
                      (3098 - 1, 3289),
                      (3290 - 1, 3385),
                      (3386 - 1, 3577),
                      (3578 - 1, 3769),
                      (3770 - 1, 3865),
                      (3866 - 1, 3961),
                      (3962 - 1, 4057),
                      (4058 - 1, 4201),
                      (4202 - 1, 4345),
                      (4346 - 1, 4537),
                      (4538 - 1, 4729),
                      (4730 - 1, 4921),
                      (4922 - 1, 5017),
                      (5018 - 1, 5209),
                      (5210 - 1, 5401),
                      (5402 - 1, 5497),
                      (8415 - 1, 8444),
                      (8445 - 1, 8474),
                      (8475 - 1, 8479),
                      (8480 - 1, 8481),
                      (8482 - 1, 8485),
                      (8486 - 1, 8549),
                      (8550 - 1, 8741),
                      (5498 - 1, 5593),
                      (5594 - 1, 5765),
                      (5766 - 1, 5937),
                      (5938 - 1, 6109),
                      (6110 - 1, 6281),
                      (6282 - 1, 6496),
                      (6497 - 1, 6582),
                      (6583 - 1, 6754),
                      (6927 - 1, 7098),
                      (7099 - 1, 7270),
                      (7271 - 1, 7356),
                      (7357 - 1, 7360),
                      (7361 - 1, 7362),
                      (7363 - 1, 7366),
                      (7367 - 1, 7558),
                      (7559 - 1, 7750),
                      (7751 - 1, 7754),
                      (7755 - 1, 7756),
                      (7757 - 1, 7760)
                      ],
    "gary_fam_pos_list": [(0,4), (6,6), (8,8)],


}
