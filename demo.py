#!/usr/bin/env python
# coding: utf-8

# # 340B Converter # #
# # contact: oce_internal_ops-d@gene.com
#
# ## Overview
#
# The purpose of this script is to take 340B files received in various formats and standardize into format suitable for
# database consumption.


import time

start_time = time.time()

from zipfile import ZipFile
from io import open

import datetime
import glob
import csv
import os
import re
import shutil
import pandas as pd

input_ = 'C:/Users/ramtekea/Documents/cld_converter_v5_latest/340B/SrcFiles/To_Process'
input_file = glob.glob(input_ + '/*.*')
output_path = 'C:/Users/ramtekea/Documents/cld_converter_v5_latest/340B/Output/'
archive_path = 'C:/Users/ramtekea/Documents/cld_converter_v5_latest/340B/Archive/'
f_map = 'C:/Users/ramtekea/Documents/cld_converter_v5_latest/340B/Config_files/File_mapping/'
today = datetime.datetime.now()
year = datetime.datetime.today().year


def file_1(fl, fl_nm, fl_map):
    df = pd.read_excel(fl, header=2, dtype=object, keep_default_na=False)
    df, df_map = func_map(df, fl_map)
    col_add, col_pos = func_add_col(df_map)
    if len(col_add) == len(col_pos):
        print('Adding column {} at {} location.'.format(col_add, col_pos))
        for col, pos in map(None, col_add, col_pos):
            df.insert(int(pos), col, '')
    else:
        print('Incorrect column positions for {} in file mapping'.format(fl_nm))
    # df.insert(49, 'Contract Identifier', '')
    df = df.fillna('')
    dt_cols = func_format(df_map)
    for col in dt_cols:
        df[col] = pd.to_datetime(df[col])
        df[col] = df[col].dt.strftime('%m/%d/%Y').apply(lambda x: None if x == "NaT" else x)
    df.to_csv(output_path + (os.path.splitext(fl_nm)[0]) + '.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_2(fl, fl_nm, fl_map):
    df = pd.read_excel(fl, header=3, dtype=object, keep_default_na=False)
    df, df_map = func_map(df, fl_map)
    df = df.fillna('')
    dt_cols = func_format(df_map)
    for col in dt_cols:
        df[col] = pd.to_datetime(df[col])
        df[col] = df[col].dt.strftime('%m/%d/%Y').apply(lambda x: None if x == "NaT" else x)
    df.to_csv(output_path + 'OPACP_DAILY_SEARCH.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_3(fl, fl_nm, fl_map):
    df = pd.read_excel(fl, header=3, dtype=object, keep_default_na=False)
    df = func_map(df, fl_map)
    df = df[0].fillna('', inplace=False)
    df.to_csv(output_path + 'OPACE_DAILY_SEARCH.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_4(fl, fl_nm, fl_map):
    df = pd.read_csv(fl, header=0, encoding='cp1252', dtype=object, keep_default_na=False)
    df = func_map(df, fl_map)
    df = df[0].fillna('', inplace=False)
    df.to_csv(output_path + (os.path.splitext(fl_nm)[0]) + '.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_5(fl, fl_nm, fl_map):
    df = pd.read_excel(fl, header=2, dtype=object, keep_default_na=False)
    df, df_map = func_map(df, fl_map)
    df = df.fillna('', inplace=False)
    dt_cols = func_format(df_map)
    for col in dt_cols:
        df[col] = pd.to_datetime(df[col])
        df[col] = df[col].dt.strftime('%m/%d/%Y').apply(lambda x: None if x == "NaT" else x)
    if re.findall(r'MedicaidExclusionFile\d{4}0[1-3]\d\d.xlsx', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = fl_nm1[:21] + '_' + fl_nm1[21:25] + '0401' + fl_nm1[30:]
    elif re.findall(r'MedicaidExclusionFile\d{4}0[4-6]\d\d.xlsx', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = fl_nm1[:21] + '_' + fl_nm1[21:25] + '0701' + fl_nm1[30:]
    elif re.findall(r'MedicaidExclusionFile\d{4}0[7-9]\d\d.xlsx', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = fl_nm1[:21] + '_' + fl_nm1[21:25] + '1001' + fl_nm1[30:]
    elif re.findall(r'MedicaidExclusionFile\d{4}1[0-2]\d\d.xlsx', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = fl_nm1[:21] + '_' + str(year) + '0101' + fl_nm1[30:]
    else:
        print('Invalid Quarter in filename of {}.'.format(fl_nm1))
    df.to_csv(output_path + (os.path.splitext(fl_nm1)[0]) + '.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_6(fl, fl_nm, fl_map):
    df = pd.read_excel(fl, header=0, dtype=object, keep_default_na=False)
    df = df.fillna('')
    df, df_map = func_map(df, fl_map)
    dt_cols = func_format(df_map)
    for col in dt_cols:
        df[col] = pd.to_datetime(df[col])
        df[col] = df[col].dt.strftime('%m/%d/%Y').apply(lambda x: None if x == "NaT" else x)
    df = df.fillna('', inplace=False)
    if re.findall(r'january', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = 'HRSA_ORPHAN_DRUG_LIST_' + fl_nm1[39:] + '0101'
    elif re.findall(r'april', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = 'HRSA_ORPHAN_DRUG_LIST_' + fl_nm1[39:] + '0401'
    elif re.findall(r'july', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = 'HRSA_ORPHAN_DRUG_LIST_' + fl_nm1[39:] + '0701'
    elif re.findall(r'october', fl_nm):
        fl_nm1 = (os.path.splitext(fl_nm)[0])
        fl_nm1 = 'HRSA_ORPHAN_DRUG_LIST_' + fl_nm1[39:] + '1001'
    else:
        print('Invalid Quarter in filename of {}.'.format(fl_nm1))
    df.to_csv(output_path + (os.path.splitext(fl_nm1)[0]) + '.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_9(fl, fl_nm):
    df = pd.read_csv(fl, header=0, encoding='cp1252', dtype=object, keep_default_na=False)
    df = df.fillna('')
    df.to_csv(output_path + 'MEDICARE_POS_OTHER.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_11(fl, fl_nm):
    shutil.move(fl, output_path + 'NPIDATA.csv')
    # os.system("cut -d ',' -f1-329


C: / Users / ramtekea / Documents / cld_converter_v5_latest / 340
B / Output / NPIDATA.csv > C: / Users / ramtekea / Documents / cld_converter_v5_latest / 340
B / Output / NPIDATA_new.csv
# os.system("sed -i '2045266d' C:/Users/ramtekea/Documents/cld_converter_v5_latest/340B/Output/NPIDATA.csv")
print('{} is processed & converted successfully!'.format(fl_nm))


def file_13(fl, fl_nm, fl_map):
    df = pd.read_csv(fl, header=0, encoding='cp1252', dtype=object, keep_default_na=False)
    df = func_map(df, fl_map)
    df = df[0].fillna('', inplace=False)
    df.to_csv(output_path + 'NUCC_TAXONOMY.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_16(fl, fl_nm, fl_map):
    df = pd.read_html(fl, header=0, keep_default_na=False)
    df = df[0]
    df = func_map(df, fl_map)
    df = df[0].fillna('', inplace=False)
    df.to_csv(output_path + (os.path.splitext(fl_nm)[0]) + '.csv', index=False, encoding='utf-8')
    print('{} is processed & converted successfully!'.format(fl_nm))


def file_18(fl, fl_nm):
    shutil.copyfile(fl, output_path + 'MSA.csv')
    print('{} is processed & converted successfully!'.format(fl_nm))


def func_map(df, fl_map):
    df_map = pd.read_excel(fl_map, header=0)
    _map = df_map[df_map['File Columns'].notna()]
    lst = list(_map['File Columns'])
    df = df[lst]
    for x, xrow in _map.iterrows():
        for col in df.columns:
            if xrow['File Columns'] == col:
                df = df.rename(columns={col: xrow['ETL Columns']})
    return (df, df_map)


def func_format(df_map):
    dt_cols = []
    df_map = df_map[df_map['Format'].notna()]
    df_map['Format'] = df_map['Format'].apply(lambda x: str(x).strip().upper())
    for x, xrow in df_map.iterrows():
        if xrow['Format'] == 'DATE':
            dt_cols.append(xrow['ETL Columns'])
    return dt_cols


def func_add_col(df_map):
    col = []
    pos = []
    for x, x_row in df_map.iterrows():
        if pd.isna(x_row['File Columns']) and ~pd.isna(x_row['ETL Columns']):
            col.append(x_row['ETL Columns'])
            pos.append(x)
    return col, pos


def file_move(fl):
    shutil.move(fl, archive_path)


for file in input_file:
    fl_nm = os.path.basename(file)
    if fl_nm == 'OPACE_DAILY_PUBLIC.xlsx':
        fl_map = f_map + 'OPACE_DAILY_PUBLIC.xlsx'
        file_1(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'searchgrid_\d{8}_\d{6}.xlsx', fl_nm):
        fl_map = f_map + 'OPACP_DAILY_SEARCH.xlsx'
        file_2(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'searchgrid_\d{8}_\d{6}_small.xlsx', fl_nm):
        fl_map = f_map + 'OPACE_DAILY_SEARCH.xlsx'
        file_3(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'HRSA_340B_Audit_list_\d{4}.csv', fl_nm):
        fl_map = f_map + 'HRSA_340B_Audit_list.xlsx'
        file_4(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'MedicaidExclusionFile\d{8}.xlsx', fl_nm):
        fl_map = f_map + 'MedicaidExclusionFile.xlsx'
        file_5(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'orphan-drug-list', fl_nm):
        fl_map = f_map + 'HRSA_ORPHAN_DRUG_LIST.xlsx'
        file_6(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'Provider_of_Services_File_Hospital_Non_Hospital_Facilities_Dataset_\d{4}_Q\d', fl_nm):
        with ZipFile(file, 'r') as zip:
            zip.extractall(input_)
        ip_file = glob.glob(input_ + '/*.*')
        for fl1 in ip_file:
            if re.findall(r'Provider_of_Services_File_Hospital_Non_Hospital_Facilities_Dataset_\d{4}_Q\d.csv',
                          os.path.basename(fl1)):
                file_9(fl1, os.path.basename(fl1))
            if re.findall(r'(?i)^Provider_of_Services_File_Hospital_Non_Hospital_Facilities_Dataset_',
                          os.path.basename(fl1)):
                file_move(fl1)

    elif re.findall(r'OTHER_Q\dY\d{2}.csv', fl_nm):
        file_9(file, fl_nm)
        file_move(file)

    elif re.findall(r'NPPES_Data_Dissemination_', os.path.basename(file)):
        with ZipFile(file, 'r') as zip:
            zip.extractall(input_)
        ip_file = glob.glob(input_ + '/*.*')
        for fl1 in ip_file:
            if re.findall(r'npidata_pfile_\d{8}-\d{8}.csv$', os.path.basename(fl1)):
                file_11(fl1, os.path.basename(fl1))
            elif re.findall(r'(?i)^NP', os.path.basename(fl1)):
                file_move(fl1)
            elif re.findall(r'pfile', os.path.basename(fl1)):
                file_move(fl1)

    elif re.findall(r'nucc_taxonomy_\d{3}.csv', fl_nm):
        fl_map = f_map + 'NUCC_TAXONOMY.xlsx'
        file_13(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'Search_results.xls', fl_nm):
        fl_map = f_map + 'Search_results.xlsx'
        file_16(file, fl_nm, fl_map)
        file_move(file)

    elif re.findall(r'cbsatocountycrosswalk.csv', fl_nm):
        file_18(file, fl_nm)
        file_move(file)

if len(next(os.walk(archive_path))[2]) >= 1:
    os.mkdir(os.path.join(archive_path, today.strftime("%m%d%y_%H%M%S")))
    for file in glob.glob(archive_path + '*.*'):
        shutil.move(file, os.path.join(archive_path, today.strftime("%m%d%y_%H%M%S")))

print("--- %s seconds ---" % (time.time() - start_time))

