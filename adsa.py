#!/usr/bin/env python
# coding: utf-8

# # CLD Converter # #
# # contact: mcdm_data_stewards-d@gene.com,mdi_ops-d@gene.com
#
# ## Overview
#
# The purpose of this script is to take Medicaid Claim Level Data received in various formats and standardize into one format suitable for database consumption.


import os
import sys

sys.path.append('/usr/lib/python2.6/site-packages/')
import pandas as pd
import numpy as np
import glob as glob
import ntpath
import shutil
import re
import csv
from tabulate import tabulate
import smtplib
from datetime import date
from datetime import datetime
from pathlib import Path

pd.options.display.max_columns = None
pd.options.display.max_rows = None
# curr_dir = 'C:/Users/singhj50/Documents/cld_converter_v5_latest'
curr_dir = os.getcwd()
startTime = datetime.now()
PMRootDir = os.environ['PMRootDir']
# sender="gcoi_mdi_ops-d@gene.com" --
# mdi_ops_receivers="mdi_ops-d@gene.com" --
sender = "motipwaa@gene.com"
mdi_ops_receivers = "motipwaa@gene.com"
# mdi_ops_receivers="srinivr7@gene.com"
# mdi_cci_receivers="mdi_users_it_cci-d@gene.com" --
# mdi_cci_receivers="singhj50@gene.com"
mdi_cci_receivers = "motipwaa@gene.com"
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = sender
cld_succ = MIMEMultipart()
cld_succ['From'] = sender
cld_succ['To'] = mdi_cci_receivers
smtpObj = smtplib.SMTP('mailhostint.roche.com')
run_parameter = str(sys.argv[1])
# run_parameter = 'VALIDATOR'
# run_parameter = 'CONVERTER'

## start Logs ###
if (run_parameter == 'CONVERTER'):
    log_success = open(curr_dir + '/outputs/logs/' + date.today().strftime("%Y%m%d") + '_converter_success.txt', 'a')
    log_success.write('Script cldcv6 starting at ' + datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + '\n')
    log_success.write('Job started with run_parameter: ' + run_parameter + '\n' + '\n')
if os.path.isfile(curr_dir + "/outputs/logs/" + date.today().strftime("%Y%m%d") + '_validator.txt'):
    os.remove(curr_dir + "/outputs/logs/" + date.today().strftime("%Y%m%d") + '_validator.txt')
log_validation = open(curr_dir + "/outputs/logs/" + date.today().strftime("%Y%m%d") + '_validator.txt', 'a')
log_validation.write(
    'Script CLD-Validator starting at ' + datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + '\n')
log_validation.write('Job started with run_parameter: ' + run_parameter + '\n' + '\n')

### load all configuration files ###
adhoc_trigger = 'N'
try:
    adhoc_trigger_df = pd.read_excel('adhoc/adhoc_trigger.xlsx')
    adhoc_trigger = adhoc_trigger_df.iloc[0]['ADHOC_TRIGGER']
    print('Running Adhoc evaluation')
except OSError:
    print('Adhoc trigger not set- running standard evaluation')

# state MDI config file
if adhoc_trigger == 'Y':
    state_cats = pd.read_excel('adhoc/config_files/mdi_adhoc_config_setup.xlsx', header=[1])
    state_cats['head_lvl'] = state_cats['head_lvl'].fillna(0)
    adhoc_map_overrides = pd.read_excel('adhoc/config_files/mdi_adhoc_state_map_overrides.xlsx')
    adhoc_map_overrides.columns = adhoc_map_overrides.columns.str.upper()
else:
    state_cats = pd.read_excel(curr_dir + '/inputs/config_files/mdi_cld_config_setup.xlsx', header=1)
    state_cats['head_lvl'] = state_cats['head_lvl'].fillna(0)

state_cats_upper = state_cats.copy()
state_cats_upper.columns = state_cats.columns.str.upper()
state_cats_upper = state_cats_upper.apply(lambda x: x.astype(str).str.upper())
state_cats_upper['HEAD_LVL'] = state_cats_upper['HEAD_LVL'].astype(float)
state_cats_upper['HEAD_LVL'] = state_cats_upper['HEAD_LVL'].astype(int)

# process quarter
if adhoc_trigger == 'Y':
    process_qtr_df = pd.read_excel('adhoc/config_files/mdi_adhoc_config_setup.xlsx', header=None)
    process_qtr = process_qtr_df.iloc[0, 1]

else:
    process_qtr_df = pd.read_excel(curr_dir + '/inputs/config_files/mdi_cld_config_setup.xlsx', header=None)
    process_qtr = process_qtr_df.iloc[0, 1]

# conversion factors by state & conversion exception lists
convert_factor = pd.read_excel(curr_dir + '/inputs/config_files/mdi_conversion_factor.xlsx',
                               header=0, converters={'NDC': lambda x: str(x)})
convert_factor.columns = convert_factor.columns.str.upper()
convert_factor['NDC'] = convert_factor['NDC'].str.strip()
convert_factor['HCPCS_NCPDP'] = convert_factor['HCPCS_CF'] * convert_factor['NCPDP_CF']
convert_factor['FINAL_CF'] = np.where(convert_factor['HCPCS_NCPDP'].isnull(), convert_factor['HCPCS_CF'],
                                      convert_factor['HCPCS_NCPDP'])

convert_factor_exceptions = pd.read_excel(curr_dir + '/inputs/config_files/mdi_conversion_program_exception.xlsx',
                                          header=0,
                                          converters={'ndc': lambda x: str(x), 'labeler_name': lambda x: str(x)})
convert_factor_exceptions.columns = convert_factor_exceptions.columns.str.upper()
convert_factor['OPERATOR'] = convert_factor['MULTIPLIER OR DIVISOR?'].apply(lambda x: '*' if x == 'Multiplier' else '/')
convert_factor = convert_factor[['STATE', 'NDC', 'OPERATOR', 'FINAL_CF']]

cf_exceptions_ndc_lvl = convert_factor_exceptions[~convert_factor_exceptions['NDC'].isnull()].copy()
cf_exceptions_ndc_lvl.rename(columns={'NDC': 'NDC_DROP'}, inplace=True)
cf_exceptions_config_lvl = convert_factor_exceptions[~convert_factor_exceptions['NDC'].notnull()].copy()
cf_exceptions_config_lvl = cf_exceptions_config_lvl[['STATE', 'PROG_NAME', 'LABELER_NAME'
    , 'INVC_QTR', 'RBT_QTR', 'EXCEPT_TYPE', 'CONVERSION_EXCEPT']].drop_duplicates()

####################################NEED TO ADD HEAD LEVEL TO PROGRAM CONFIG OVERRIDES########################################

# program or labeler level mapping overrides
mapping_overrides = pd.read_excel(curr_dir + '/inputs/config_files/mdi_cld_program_map_override.xlsx',
                                  converters={'LABELER_NAME': lambda x: str(x)})
mapping_overrides.columns = mapping_overrides.columns.str.upper()


### function block ###

def qtr_assess(x, y):
    """
    parse and format year and quarter with regex. refers to dictionary: qtr_parse_dict
    expected inputs:
    x : string to be parsed
    y : file path (for error log)
    """

    quarter_raw_input = x
    curr_file_path = y

    quarter_input = os.path.splitext(quarter_raw_input)[0]
    quarter_input = ('_' + quarter_input + '_')

    qtr_raw, reg_pattern, qtr_parsed = None, None, None
    parse_qtr_raw, parse_result_list = [], []
    qtr_result = 'UNK'

    try:

        for key, value in qtr_parse_dict.items():

            curr_parse_key = key
            curr_reg_pattern = value

            try:

                parse_qtr_raw = re.findall(curr_reg_pattern, quarter_input)

                for qtr in parse_qtr_raw:
                    parse_result_list.append([quarter_input, qtr, curr_parse_key])

            except Exception as e:
                continue

        if len(parse_result_list) < 1:
            qtr_result = 'UNK'

        else:

            parse_result_df = pd.DataFrame(parse_result_list, columns=['quarter_input', 'parsed_qtr', 'curr_parse_key'])
            parse_result_df['qtr_result'] = parse_result_df.apply(
                lambda x: qtr_standardize(x['parsed_qtr'], x['curr_parse_key']), axis=1)
            parse_result = parse_result_df[['qtr_result']].drop_duplicates()

            if len(parse_result) > 1:  # check for duplicate results and override to UNK
                qtr_result = 'UNK'
            else:
                qtr_result = parse_result['qtr_result'].values[0]

        return qtr_result

    except Exception as e:
        print('Quarter assessment error for ' + curr_file_path + ' with error ' + str(repr(e)))
        # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Quarter assessment error for ' + ' ' + curr_file_path + str(repr(e)) + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' Quarter assessment error for ' + ' ' + curr_file_path + str(
            repr(e)) + '\n')


def qtr_standardize(x, y):
    parsed_qtr = x
    parse_key = y

    if parse_key == 'NQYYYY':
        qtr_final = parsed_qtr[2:6] + 'Q' + parsed_qtr[0]

    elif parse_key == 'NQYY':
        qtr_final = '20' + parsed_qtr[3:5] + 'Q' + parsed_qtr[1]

    elif parse_key == '/YYYYN/':
        qtr_final = parsed_qtr[1:5] + 'Q' + parsed_qtr[5]

    elif parse_key == 'YYYYQN':
        qtr_final = parsed_qtr.upper()

    elif parse_key == 'YYQN':
        qtr_final = '20' + parsed_qtr[1:3] + 'Q' + parsed_qtr[4]

    elif parse_key == 'QNYY':
        qtr_final = '20' + parsed_qtr[3:5] + 'Q' + parsed_qtr[2]

    elif parse_key == 'NYYYY':
        qtr_final = parsed_qtr[2:6] + 'Q' + parsed_qtr[1]

    elif parse_key == 'QNYYYY':
        qtr_final = parsed_qtr[2:6] + 'Q' + parsed_qtr[1]

    elif parse_key == 'YYYYN_':
        qtr_final = parsed_qtr[0:4] + 'Q' + parsed_qtr[4]

    elif parse_key == 'YYYY_N_':
        qtr_final = parsed_qtr[0:4] + 'Q' + parsed_qtr[5]

    elif parse_key == 'YYYY/N':
        qtr_final = parsed_qtr[0:4] + 'Q' + parsed_qtr[5]

    elif parse_key == 'YYYYN':
        qtr_final = parsed_qtr[0:4] + 'Q' + parsed_qtr[4]

    elif parse_key == 'MULTI':
        qtr_final = 'UNK'

    else:
        qtr_final = None

    return qtr_final.upper()


def ndc_assess(x, y, z):
    """
    parse ndc using regex- refers to dictionary: ndc_parse_dict
    expected inputs:
    x : string to be parsed
    y : labeler
    z : file path (for error log)
    """

    parse_key = None

    ndc_input = x
    curr_labeler = y
    curr_file_path = z

    ndc = 'UNK'

    try:

        for key, value in ndc_parse_dict.items():

            curr_parse_key = key
            curr_reg_pattern = value

            parse_ndc = None
            parse_ndc = re.compile(curr_reg_pattern)

            try:

                ndc_raw = parse_ndc.findall(ndc_input)[0]
                parse_key = curr_parse_key

                if parse_key == 'NNNNN-NNNN-NN':
                    break

                elif parse_key == 'NNNNNNNNNNN':
                    break

            except:
                continue

        if parse_key != None:

            if parse_key == 'NNNNN-NNNN-NN':
                ndc = ndc_raw[0:5] + ndc_raw[6:10] + ndc_raw[11:13]

            elif parse_key == 'NNNNNNNNNNN':
                ndc = ndc_raw

            elif parse_key == 'NNNN-NN':
                ndc = curr_labeler + ndc_raw[0:4] + ndc_raw[5:7]

    except Exception as e:
        print('NDC file level assessment error for ' + curr_file_path + ' with error ' + str(repr(e)))
        # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' NDC file level assessment error for ' + ' ' + curr_file_path + str(repr(e)) + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' NDC file level assessment error for ' + ' ' + curr_file_path + str(
            repr(e)) + '\n')

    return ndc


def unit_convert(x, y, z):
    """
    unit conversion for configured states/NDCs
    expected inputs:
    x : units to be converted
    y : conversion factor
    z : operater (* or /)
    """

    try:

        if z == '*':
            converted_inv_qty = x * y

        elif z == '/':
            converted_inv_qty = x / y

        else:
            converted_inv_qty = x

    except Exception as e:
        print('Unit conversion error (could not convert units) for: ' + curr_file_path + ' with error ' + str(repr(e)))
        # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Unit conversion error (could not convert units) for ' + curr_file_path + str(repr(e)) + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' Unit conversion error (could not convert units) for ' + curr_file_path + str(
            repr(e)) + '\n')
    return converted_inv_qty


def parse_col_npi(x):
    npi_reg = '([0-9]{10})'

    col_npi = x

    try:
        parsed_npi = None
        parsed_npi_orig = re.compile(npi_reg)

        parsed_npi = parsed_npi_orig.findall(col_npi)[0]

    except Exception as e:
        parsed_npi = ''

    return parsed_npi


def exclude_file(config_row, process_qtr):
    exclude_descrip = None

    if config_row['RBT_QTR'] == 'UNK':
        exclude_descrip = 'Rebate Quarter Issue :Either No or Duplicate Rebate Quarters present in the file name.'
        return pd.Series(['Y', exclude_descrip])
    elif config_row['FILE_FORMAT'] == 'UNK':
        exclude_descrip = 'File format error'
        return pd.Series(['Y', exclude_descrip])
    elif config_row['NDC'] == 'UNK':
        exclude_descrip = 'Could not identify NDC from file name. Please check file name'
        return pd.Series(['Y', exclude_descrip])
    # elif config_row['INVC_QTR'] != process_qtr:
    # exclude_descrip = 'Invoice quarter is outside of configured processing quarter'
    # return pd.Series(['Y', exclude_descrip])
    elif config_row['ACTIVE_CONFIG'] != 'Y':
        exclude_descrip = 'This state is not configured, or configuration is turned off'
        return pd.Series(['Y', exclude_descrip])
    else:
        return pd.Series(['N', exclude_descrip])


def add_status_issue(cld_file, issue_descrip):
    if issue_descrip == None:
        issue_descrip = 'Undefined error'

    file_error_desc = pd.DataFrame(
        {"STATE": [cld_file.STATE], "LABELER_NAME": [cld_file.LABELER_NAME], "PROG_NAME": [cld_file.PROG_NAME],
         "FILE_NAME": [cld_file.FILE_NAME], "EXCLUDE_DESCRIP": [issue_descrip]})

    return file_error_desc


def validation_status_email():
    if len(error_files) > 0 and len(cld_run_summary_build) > 0:
        error_files['STATE'] = error_files['STATE'].fillna('?')
        error_states = (', '.join(list(error_files['STATE'].drop_duplicates())))
        text = """
        Hello Team,\n\n 

        Validation Status Below   :\n

        <br>{table}

        Regards,
        CLD-Validator"""

        html = """
        <html>
        <head>
        <style> 
          table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
          th, td {{ padding: 5px; }}
        </style>
        </head>
        <body><p>
        Hello Team,<br></p>
        <p>Please find Validation Summary  Below    :</p>
        {table}
        <br>
        <p>***** This is an automated alert from MDI Cld Validator *****<br>For questions regarding this message, please contact : mdi_ops-d@gene.com<br>

           </p>
        </body></html>
"""

        with open(curr_dir + '/outputs/logs/' + process_qtr + '_cld_validation.csv') as input_file:
            reader = csv.reader(input_file)
            data = list(reader)
        msg['Subject'] = "MDI : Cld Validator -  Failure Alert : " + error_states
        msg['To'] = mdi_cci_receivers
        text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
        html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))
        message = msg.attach(MIMEMultipart("alternative", None, [MIMEText(text), MIMEText(html, 'html')]))
        text = msg.as_string()
        smtpObj.sendmail(sender, mdi_cci_receivers, text)
    ## Mail for Converter Part in case of no files###
    if len(cld_run_summary_build) == 0 and run_parameter == 'CONVERTER':
        msg['Subject'] = "MDI : Cld Converter  - Success"
        msg['To'] = mdi_ops_receivers
        message = "Hi, No Files Found for Conversion at  " + datetime.strftime(datetime.now(),
                                                                               '%m/%d/%Y %H:%M:%S') + '\n'
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()
        smtpObj.sendmail(sender, mdi_ops_receivers, text)
    ## Mail for Converter Part for succesfully uploaded files###
    if len(cld_validation_success) > 0 and (run_parameter == 'CONVERTER'):
        success_email = open(
            curr_dir + '/outputs/status_email/' + date.today().strftime("%Y%m%d") + '_success_upload_email.txt', 'w')
        success_email.write('Hi Team,' + '\n' + '\n')
        success_email.write(
            'Below file(s) are ready to be consumed.It will be uploaded to MDI in the next scheduled run.  ' + '\n' + '\n')
        for file in cld_validation_success.itertuples():
            success_email.write(file.STATE + ' : ' + file.FILE_NAME + '\n')
        success_email.write('\n' + '***** This is an automated alert from MDI Cld Converter *****' + '\n')
        success_email.write('For questions regarding this message, please contact : mdi_ops-d@gene.com')
        success_email.close()
        log_success.write('File Write complete  : ' + '\n')
        cld_succ['Subject'] = "MDI : CLD Conversion Upload Success"
        send_succ_mail = open(
            curr_dir + "/outputs/status_email/" + date.today().strftime("%Y%m%d") + '_success_upload_email.txt', "r")
        succ_email_content = send_succ_mail.read()
        cld_succ.attach(MIMEText(succ_email_content, 'plain'))
        text = cld_succ.as_string()
        log_success.write('Sending Success upload mail  : ' + '\n')
        smtpObj.sendmail(sender, mdi_cci_receivers, text)


# In[54]:

# file format mappings

mag_ffs_read_cols = pd.read_excel(curr_dir + '/inputs/file_format_mapping_sets/magellan_ffs.xlsx')
mag_mco_read_cols = pd.read_excel(curr_dir + '/inputs/file_format_mapping_sets/magellan_mco.xlsx')
std_read_cols = pd.read_excel(curr_dir + '/inputs/file_format_mapping_sets/standard.xlsx')

mag_ffs_file_cols = mag_ffs_read_cols.columns.tolist()
mag_mco_file_cols = mag_mco_read_cols.columns.tolist()
std_file_cols = std_read_cols.columns.tolist()

# In[55]:


# regular expression dictionaries

qtr_parse_dict = {'MULTI': '([1-2]{1}[0-9]{3}[0-9]{1}[q,Q][1-4]{1})',
                  'NQYYYY': '([1-4]{1}[Q,q][1-2]{1}[0-9]{3})',
                  'YYYYQN': '([1-2]{1}[0-9]{3}[Q,q][1-4]{1})',
                  'QNYYYY': '([Q,q][1-4]{1}[1-2]{1}[0-9]{3})',
                  'YYQN': '(\D[0-9]{2}[Q,q][1-4]{1}\D)',
                  'NQYY': '(\D[1-4]{1}[Q,q][0-9]{2}\D)',
                  '/YYYYN/': '(\D[1-2]{1}[0-9]{3}[1-4]{1}\D)',
                  'QNYY': '(\D[Q,q][1-4]{1}[0-9]{2}\D)',
                  'NYYYY': '(\D[1-4]{1}20[0-9]{2}\D)',
                  'YYYY_N_': '([1-2]{1}[0-9]{3}[_][1-4]{1}[_])',
                  'YYYY/N': '([1-2]{1}[0-9]{3}[/][1-4]{1})'
                  }

ndc_parse_dict = {'NNNNN-NNNN-NN': '([0-9]{5}[-][0-9]{4}[-][0-9]{2})',
                  'NNNNNNNNNNN': '([0-9]{11})',
                  'NNNN-NN': '([0-9]{4}[-][0-9]{2})'}

col_spec_dict = {
    'DE_COL_SPEC': [(0, 11), (11, 12), (12, 25), (25, 26), (26, 30), (30, 36), (36, 51), (51, 55), (55, 63), (63, 71),
                    (71, 75), (75, 89), (89, 100), (100, 111), (111, 122), (122, 123), (123, 134), (134, 142)],
    'OR_COL_SPEC': [(0, 13), (13, 26), (26, 37), (37, 42), (42, 58), (58, 66), (66, 74), (74, 89), (89, 104),
                    (104, 115), (115, 126), (126, 133), (133, 146), (146, 157), (157, 169), (169, 173), (173, 175)],
    'MS_COL_SPEC': [(0, 10), (10, 11), (11,24), (24,25), (25,29), (29,34), (34,35), (35,45), (45,50),
                    (50,54), (54,62), (62,70), (70,74), (74,88), (88,102), (102,113), (113,124),(124,135),(135,136),(136,147),(147,155)]
}

### create custom headers dict ###

if adhoc_trigger == 'Y':
    header_file_list = glob.glob('adhoc/adhoc_mapping_sets/HEADER/*.*')
else:
    header_file_list = glob.glob(curr_dir + '/inputs/state_mapping_sets/HEADER/*.*')

custom_header_dict = dict()

for header_file in header_file_list:
    custom_header = pd.read_excel(header_file, header=None)
    custom_header = custom_header.values.tolist()
    custom_header = [item for sublist in custom_header for item in sublist]

    head_name = Path(os.path.splitext(header_file)[0]).name

    custom_header_dict[head_name] = custom_header

# create state file mappings

if adhoc_trigger == 'Y':
    state_mapping_list = glob.glob('adhoc/adhoc_mapping_sets/*.*')
else:
    state_mapping_list = glob.glob(curr_dir + '/inputs/state_mapping_sets/STD/*.*')

state_map_dict = dict()

for state in state_mapping_list:

    st_path = state
    st = Path(os.path.splitext(state)[0]).name
    st_format = Path(state).parts[-2]

    if adhoc_trigger == 'Y':
        map_name = st + '_STD_MAP'

    else:
        map_name = st + '_' + st_format + '_MAP'

    map_df = pd.read_excel(st_path)
    map_df = map_df[['ORIGINAL_STATE_COLUMNS', 'MDI_STD_COLUMNS']]
    map_df = map_df.dropna(how='any')

    map_df['ORIGINAL_STATE_COLUMNS'] = map_df['ORIGINAL_STATE_COLUMNS'].str.strip()
    map_df['ORIGINAL_STATE_COLUMNS'] = map_df['ORIGINAL_STATE_COLUMNS'].str.upper()

    map_df = map_df.replace('\n', '', regex=True)

    map_dict = pd.Series(map_df.MDI_STD_COLUMNS.values, index=map_df.ORIGINAL_STATE_COLUMNS).to_dict()

    state_map_dict[map_name] = map_dict

# magellan mappings

if adhoc_trigger == 'Y':
    mag_mco_map = pd.read_excel('adhoc/adhoc_mapping_sets/MAG/cust_mag_mco.xlsx')
    mag_ffs_map = pd.read_excel('adhoc/adhoc_mapping_sets/MAG/cust_mag_ffs.xlsx')
    alt_mag_mco_map = pd.read_excel(curr_dir + '/inputs/state_mapping_sets/MAG/mag_mco_alternate.xlsx')
    alt_mag_ffs_map = pd.read_excel(curr_dir + '/inputs/state_mapping_sets/MAG/mag_ffs_alternate.xlsx')
else:
    mag_mco_map = pd.read_excel(curr_dir + '/inputs/state_mapping_sets/MAG/mag_mco.xlsx')
    mag_ffs_map = pd.read_excel(curr_dir + '/inputs/state_mapping_sets/MAG/mag_ffs.xlsx')
    alt_mag_mco_map = pd.read_excel(curr_dir + '/inputs/state_mapping_sets/MAG/mag_mco_alternate.xlsx')
    alt_mag_ffs_map = pd.read_excel(curr_dir + '/inputs/state_mapping_sets/MAG/mag_ffs_alternate.xlsx')

mag_mco_map = mag_mco_map.dropna(how='any')
mag_ffs_map = mag_ffs_map.dropna(how='any')
mag_mco_map['ORIGINAL_STATE_COLUMNS'] = mag_mco_map['ORIGINAL_STATE_COLUMNS'].str.strip()
mag_ffs_map['ORIGINAL_STATE_COLUMNS'] = mag_ffs_map['ORIGINAL_STATE_COLUMNS'].str.strip()

mag_mco_map['ORIGINAL_STATE_COLUMNS'] = mag_mco_map['ORIGINAL_STATE_COLUMNS'].str.upper()
mag_ffs_map['ORIGINAL_STATE_COLUMNS'] = mag_ffs_map['ORIGINAL_STATE_COLUMNS'].str.upper()

alt_mag_mco_map = alt_mag_mco_map.dropna(how='any')
alt_mag_ffs_map = alt_mag_ffs_map.dropna(how='any')
alt_mag_mco_map['ORIGINAL_STATE_COLUMNS'] = alt_mag_mco_map['ORIGINAL_STATE_COLUMNS'].str.strip()
alt_mag_ffs_map['ORIGINAL_STATE_COLUMNS'] = alt_mag_ffs_map['ORIGINAL_STATE_COLUMNS'].str.strip()

alt_mag_mco_map['ORIGINAL_STATE_COLUMNS'] = alt_mag_mco_map['ORIGINAL_STATE_COLUMNS'].str.upper()
alt_mag_ffs_map['ORIGINAL_STATE_COLUMNS'] = alt_mag_ffs_map['ORIGINAL_STATE_COLUMNS'].str.upper()

mag_mco_cols = pd.Series(mag_mco_map.MDI_MAG_COLUMNS.values, index=mag_mco_map.ORIGINAL_STATE_COLUMNS).to_dict()
mag_ffs_cols = pd.Series(mag_ffs_map.MDI_MAG_COLUMNS.values, index=mag_ffs_map.ORIGINAL_STATE_COLUMNS).to_dict()

alt_mag_mco_cols = pd.Series(alt_mag_mco_map.MDI_MAG_COLUMNS.values,
                             index=alt_mag_mco_map.ORIGINAL_STATE_COLUMNS).to_dict()
alt_mag_ffs_cols = pd.Series(alt_mag_ffs_map.MDI_MAG_COLUMNS.values,
                             index=alt_mag_ffs_map.ORIGINAL_STATE_COLUMNS).to_dict()

# create final config table for files to be processed

error_files = pd.DataFrame()
config_table = pd.DataFrame()
config_table_all = pd.DataFrame()

if adhoc_trigger == 'Y':

    state_file_list = glob.glob('adhoc/to_process/*/*/*/*/*/*.*')
#     state_file_list = glob.glob("\\\\dnafiles1\sales\MCOps\Gov't Pgms\Medicaid\STATES\CLD\MDI Directory Structure\*\*\*\*\*\*.*")

else:
    state_file_list = glob.glob("/NAS/SADMIN/cdip/DEV/MDI/CDIP/scripts/MDI-Preprocess/inputs/to_process/*/*/*/*/*/*.*")
    # state_file_list = glob.glob("/NAS/MCOps/Gov't Pgms/Medicaid/STATES/CLD/MDI Directory Structure/*/*/*/*/*/*.*") --
    # state_file_list = glob.glob(curr_dir+'/inputs/to_process/*/*/*/*/*/*.*')
#     state_file_list = glob.glob("\\\\dnafiles1\sales\MCOps\Gov't Pgms\Medicaid\STATES\CLD\MDI Directory Structure\*\*\*\*\*\*.*")

parsed_config_list = []

if len(state_file_list) > 0:

    for file_path in state_file_list:
        file_path = file_path
        file_name = Path(file_path).name

        dir_path = os.path.dirname(file_path)

        invc_qtr = Path(file_path).parts[-2]
        prog_nm = Path(file_path).parts[-3]
        st_nm = Path(file_path).parts[-6]
        labeler_nm = Path(file_path).parts[-4]
        mag_typ = Path(file_path).parts[-5]

        cols = ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'INVC_QTR', 'PROG_NAME', 'MAG_TYPE', 'ST_NM', 'LABELER_NAME']
        vals = [file_path, dir_path, file_name, invc_qtr, prog_nm, mag_typ, st_nm, labeler_nm]

        parsed_config_list.append(dict(zip(cols, vals)))
        # log_success.write(file_name + '\n')
    config_table_build = pd.DataFrame(parsed_config_list)

    if len(config_table_build) > 0:
        config_table_build['FILE_TYPE_JOIN'] = config_table_build['MAG_TYPE'].apply(
            lambda x: 'MAG' if x in ['MCO', 'FFS'] else 'STD')

    try:

        config_table_build = pd.merge(config_table_build, state_cats_upper, left_on=['ST_NM', 'FILE_TYPE_JOIN'],
                                      right_on=['STATE', 'FILE_FORMAT'], how='left')

        if len(config_table_build) > 0:

            # setup program mapping overrides
            prog_override_eval_headers = {}

            for row in range(mapping_overrides.shape[0]):

                prog_override = []

                prog_override_eval_headers[row] = mapping_overrides.iloc[[row]].dropna(axis=1)
                prog_override = prog_override_eval_headers[row]

                # find custom join conditions
                prog_override_join_values = list(prog_override_eval_headers[row])
                prog_override_join_values = [x for x in prog_override_join_values if x not in ['CUSTOM_MAP']]

                config_table_build = pd.merge(config_table_build, prog_override, on=prog_override_join_values,
                                              how='left')

                if 'CUSTOM_MAP_x' in config_table_build.columns:  # remove duplicated columns within loop
                    config_table_build['CUSTOM_MAP'] = config_table_build.CUSTOM_MAP_x.combine_first(
                        config_table_build.CUSTOM_MAP_y)
                    config_table_build.drop(['CUSTOM_MAP_x', 'CUSTOM_MAP_y'], axis=1, inplace=True)

            # setup conversion exceptions
            convert_eval_headers = {}

            for row in range(cf_exceptions_config_lvl.shape[0]):

                convert_exception = []

                convert_eval_headers[row] = cf_exceptions_config_lvl.iloc[[row]].dropna(axis=1)
                convert_exception = convert_eval_headers[row]

                # find custom join conditions
                convert_eval_join_values = list(convert_eval_headers[row])
                convert_eval_join_values = [x for x in convert_eval_join_values if
                                            x not in ['CONVERSION_EXCEPT', 'EXCEPT_TYPE']]

                config_table_build = pd.merge(config_table_build, convert_exception, on=convert_eval_join_values,
                                              how='left')

                if 'CONVERSION_EXCEPT_x' in config_table_build.columns:  # remove duplicated columns within loop
                    config_table_build['CONVERSION_EXCEPT'] = config_table_build.CONVERSION_EXCEPT_x.combine_first(
                        config_table_build.CONVERSION_EXCEPT_y)
                    config_table_build.drop(['CONVERSION_EXCEPT_x', 'CONVERSION_EXCEPT_y'], axis=1, inplace=True)

            config_table_build['CONVERSION_EXCEPT'] = config_table_build['CONVERSION_EXCEPT'].fillna('NAN')
            config_table_build['CUSTOM_MAP'] = config_table_build['CUSTOM_MAP'].fillna('NAN')

        if adhoc_trigger == 'Y':
            config_table_build = pd.merge(config_table_build, adhoc_map_overrides, left_on='ST_NM',
                                          right_on='OVERRIDE_STATE', how='left')

            config_table_build['ADHOC_MAP'] = config_table_build['ADHOC_MAP'].fillna('NAN')

        else:
            config_table_build['ADHOC_MAP'] = 'NAN'

        config_table_build['RBT_QTR'] = None
        config_table_build['RBT_QTR'] = config_table_build[config_table_build['RBT_DT_OVERRIDE'] != 'Y'].apply(
            lambda x: qtr_assess(x['FILE_NAME'], x['FILE_PATH']), axis=1)
        config_table_build['NDC'] = None
        config_table_build['NDC'] = config_table_build[config_table_build['FILENAME_AS_NDC'] == 'Y'].apply(
            lambda x: ndc_assess(x['FILE_NAME'], x['LABELER_NAME'], x['FILE_PATH']), axis=1)

        config_table = config_table_build[
            ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'ACTIVE_CONFIG', 'STATE', 'LABELER_NAME', 'PROG_NAME', 'INVC_QTR',
             'RBT_QTR',
             'FILE_FORMAT', 'HEAD_LVL', 'MAG_TYPE', 'FILE_CONVERT_TYPE', 'DELIM', 'CUSTOM_MAP', 'HEADER_NAME',
             'LIMIT_ON', 'TABS_AS_NDC', 'FILENAME_AS_NDC', 'NDC', 'SKIP_TAB',
             'MULTI_HEAD', 'USE_CONVERT_FILE', 'RBT_DT_OVERRIDE', 'INV_DT_OVERRIDE',
             'PARSE_NPI', 'ADHOC_MAP', 'TABS_AS_RBT_QTR', 'CONVERSION_EXCEPT']]

        config_table['EXCLUDE_FILE'] = None
        config_table['EXCLUDE_DESCRIP'] = None
        config_table[['EXCLUDE_FILE', 'EXCLUDE_DESCRIP']] = config_table.apply(lambda x: exclude_file(x, process_qtr),
                                                                               axis=1)

        config_table_all = config_table.copy()

        config_table.to_excel(curr_dir + '/temp/last_run_config_table_all.xlsx')

        excluded_rbt_qtr = config_table[config_table['RBT_QTR'] == 'UNK']
        excluded_rbt_qtr[
            'EXCLUDE_DESCRIP'] = 'Rebate Quarter Issue :Either No or Duplicate Rebate Quarters present in the file name.'

        excluded_ndc = config_table[config_table['NDC'] == 'UNK']
        excluded_ndc['EXCLUDE_DESCRIP'] = 'Could not identify NDC from file name. Please check file name'

        # excluded_invc_qtr = config_table[config_table['INVC_QTR'] != process_qtr]
        # excluded_invc_qtr['EXCLUDE_DESCRIP'] = 'Invoice quarter is outside of configured processing quarter'

        excluded_actv_config = config_table[config_table['ACTIVE_CONFIG'] != 'Y']
        excluded_actv_config['EXCLUDE_DESCRIP'] = 'This state is not configured, or configuration is turned off'

        excluded_files = excluded_rbt_qtr
        excluded_files = excluded_files.append(excluded_ndc)
        # excluded_files = excluded_files.append(excluded_invc_qtr)
        excluded_files = excluded_files.append(excluded_actv_config)

        error_files = excluded_files[['STATE', 'LABELER_NAME', 'PROG_NAME', 'FILE_NAME', 'EXCLUDE_DESCRIP']]

        config_table = config_table[config_table['RBT_QTR'] != 'UNK']
        config_table = config_table[config_table['FILE_FORMAT'] != 'UNK']
        config_table = config_table[config_table['NDC'] != 'UNK']
        config_table = config_table[
            config_table['INVC_QTR'] == process_qtr]  # limit processing to configured invoice quarter
        config_table = config_table[config_table['ACTIVE_CONFIG'] == 'Y']

        config_table.to_excel(curr_dir + '/temp/last_run_config_table.xlsx')
        excluded_files.to_excel(curr_dir + '/temp/last_run_excluded.xlsx')

    except Exception as e:
        print(e)
        config_table = pd.DataFrame()
        # log_success.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Did not build config table- no files to process' + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' Did not build config table- no files to process' + '\n')
else:
    print('Did not build config table- no files to process')
    # log_success.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Did not build config table- no files to process' + '\n')
    log_validation.write(datetime.strftime(datetime.now(),
                                           '%m/%d/%Y %H:%M:%S') + ' Did not build config table- no files to process' + '\n')


def cld_read(cld_file, error_dict):
    df_dict, df = {}, ()
    alt_mag_trigger, read_result, cld_sheet, read_error_descrip = 'N', 'SUCCESS', 'Unassigned', 'None'
    # print(cld_file)
    try:

        if cld_file.FILE_CONVERT_TYPE == 'CSV':

            cld_sheet = 'DELIMITED'

            if cld_file.HEADER_NAME != 'NAN':
                df = pd.read_csv(cld_file.FILE_PATH
                                 , delimiter=cld_file.DELIM
                                 , header=None
                                 , names=custom_header_dict[cld_file.HEADER_NAME]
                                 , dtype=str
                                 , skipinitialspace=True)

            else:
                df = pd.read_csv(cld_file.FILE_PATH
                                 , delimiter=cld_file.DELIM
                                 , header=int(cld_file.head_lvl)
                                 , dtype=str
                                 , skipinitialspace=True)

            if df.empty == True:
                read_result, read_error_descrip = 'ERROR_EMPTY_DF', 'File is  empty:no claims found'

            df_dict[cld_sheet] = df

        elif cld_file.FILE_CONVERT_TYPE == 'FIXED_WIDTH':

            cld_sheet = 'FIXED_WIDTH'

            df = pd.read_fwf(cld_file.FILE_PATH
                             , colspecs=col_spec_dict[cld_file.DELIM]
                             , names=custom_header_dict[cld_file.HEADER_NAME]
                             , dtype=str
                             , skipinitialspace=True)

            if df.empty == True:
                read_result, read_error_descrip = 'ERROR_EMPTY_DF', 'File is empty:no claims found'

            df_dict[cld_sheet] = df

        elif cld_file.FILE_FORMAT == 'MAG':

            cld_sheet = 'Magellan'
            mag_sheet_test = pd.ExcelFile(cld_file.FILE_PATH).sheet_names

            for mag_sheet in mag_sheet_test:
                if 'Financial Data' in mag_sheet:
                    alt_mag_trigger = 'Y'
                    use_mag_sheet = mag_sheet

            if alt_mag_trigger == 'Y':
                df = pd.read_excel(cld_file.FILE_PATH
                                   , header=4
                                   , dtype=str
                                   , sheet_name=use_mag_sheet
                                   , skipinitialspace=True)


            else:
                df = pd.read_excel(cld_file.FILE_PATH
                                   , header=int(cld_file.HEAD_LVL)
                                   , dtype=str
                                   , skipinitialspace=True)

            if df.empty == True:
                read_result, read_error_descrip = 'ERROR_EMPTY_DF', 'File  is empty:no claims found'

            df_dict[cld_sheet] = df

        else:

            cld_sheet_list = pd.ExcelFile(cld_file.FILE_PATH).sheet_names

            for cld_sheet in cld_sheet_list:

                if cld_file.SKIP_TAB == 'Y':

                    skip_sheet = False
                    skip_sheet_list = ['Summary', 'HCPCS', 'Document', 'Evaluation']

                    for item in skip_sheet_list:
                        if item in cld_sheet:
                            skip_sheet = True
                            # print('Skipping sheet: ' + cld_file.FILE_NAME + ' [' + cld_sheet + ']')

                    if skip_sheet == True:
                        continue

                if cld_file.MULTI_HEAD != 'NAN':

                    hdr_string = cld_file.MULTI_HEAD
                    hdr_list = hdr_string.split(",")
                    hdr_list_cvrt = list(map(int, hdr_list))

                    df = pd.read_excel(cld_file.FILE_PATH
                                       , header=hdr_list_cvrt
                                       , sheet_name=cld_sheet
                                       , dtype=str
                                       , skipinitialspace=True)

                    a = df.columns.get_level_values(level=0).str.replace('Un.*', 'LW')
                    a = a.str.strip()
                    b = df.columns.get_level_values(level=1).str.replace('Un.*', 'UP')
                    b = b.str.strip()

                    df.columns = [a, b]
                    df.columns = df.columns.map('_'.join)

                else:
                    df = pd.read_excel(cld_file.FILE_PATH
                                       , header=int(cld_file.HEAD_LVL)
                                       , sheet_name=cld_sheet
                                       , dtype=str
                                       , skipinitialspace=True)

                if df.empty == True:  # skip blank sheets
                    continue

                df_dict[cld_sheet] = df

        if bool(df_dict) == False:
            read_result, read_error_descrip = 'ERROR_DICT_EMPTY', 'File Found was empty'

        if 'ERROR' in read_result:
            raise ValueError(read_error_descrip)
        if 'SUCCESS' in read_result:
            log_validation.write(datetime.strftime(datetime.now(),
                                                   '%m/%d/%Y %H:%M:%S') + ' CLD_READ Validation passed for ' + cld_file.FILE_NAME + ' [' + cld_sheet + ']: ' + '\n')
        df_dict, read_result, error_dict = cld_read_special(df_dict, cld_file, read_result, error_dict)

    except Exception as e:
        if read_result == 'SUCCESS':
            read_result = 'ERROR'
        error_dict['read_error'][cld_file.STATE + ' ' + cld_file.FILE_NAME] = df
        # read_result, read_error_descrip = 'ERROR_READ', 'Unsupported format,corrupt file or Password Protected'
        # print('Read error with ' + cld_file.FILE_NAME + ' [' + cld_sheet + ']: ' + str(repr(e)))
        if (read_error_descrip == 'None'):
            read_error_descrip = str(repr(e))

        if (read_error_descrip == "TypeError('sequence item 0: expected str instance, float found')"):
            read_error_descrip = 'Error Reading Header of the File'
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' Read error with ' + cld_file.FILE_NAME + ' [' + cld_sheet + ']: ' + read_error_descrip + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' CLD_READ Validation FAILED for ' + cld_file.FILE_NAME + ' [' + cld_sheet + ']: ' + '\n')
    return df_dict, alt_mag_trigger, read_result, read_error_descrip, error_dict


def cld_read_special(df_dict, cld_file, read_result, error_dict):
    read_special_result, read_special_desc = read_result, None
    df_spcl_read_dict = {}

    try:

        for cld_sheet, df in df_dict.items():

            if cld_file.STATE == 'ND':  # ND header start is row not consistent, header row needs to be found before reading

                for sheet in range(19):
                    for i, row in df.iterrows():
                        if row.notnull().all():
                            fixed_df = df.iloc[(i + 1):].reset_index(drop=True)
                            fixed_df.columns = list(df.iloc[i])

                            df_spcl_read_dict[cld_sheet] = fixed_df
                            break

                        else:
                            df_spcl_read_dict[cld_sheet] = df

            elif cld_file.STATE == 'WI':
                if 'LW_UP' in df.columns:
                    df = df.drop('LW_UP', axis=1)
                    df_spcl_read_dict[cld_sheet] = df
            if cld_file.STATE == 'CT':
                ct_get_ndc_df = pd.read_excel(cld_file.FILE_PATH, sheet_name=cld_sheet)
                ct_raw_ndc = ct_get_ndc_df.iloc[1][1]
                ndc_assess_df = pd.DataFrame(
                    {"RAW_NDC": ct_raw_ndc, "LABELER_NAME": cld_file.LABELER_NAME, "FILE_PATH": cld_file.FILE_PATH},
                    index=[0])
                ct_ndc_assessed = ndc_assess_df.apply(
                    lambda x: ndc_assess(x['RAW_NDC'], x['LABELER_NAME'], x['FILE_PATH']), axis=1)
                df['NDC11'] = ct_ndc_assessed[0]
                df_spcl_read_dict[cld_sheet] = df


            else:

                df_spcl_read_dict[cld_sheet] = df

        if bool(df_spcl_read_dict) == False:
            read_special_result, read_special_desc = 'ERROR_DICT_EMPTY', 'Empty dictionary after special read'

        if 'ERROR' in read_special_result:
            raise ValueError(read_special_desc)
        if 'SUCCESS' in read_special_result:
            log_validation.write(datetime.strftime(datetime.now(),
                                                   '%m/%d/%Y %H:%M:%S') + ' CLD_SPECIAL_READ Validation passed for ' + cld_file.FILE_NAME + ' [' + cld_sheet + ']: ' + '\n')
    except Exception as e:
        read_special_result = 'READ_SPECIAL_ERROR'
        error_dict['read_error'][cld_file.STATE + ' ' + cld_file.FILE_NAME] = df
        # print('Read (special) error with ' + cld_file.FILE_NAME + ' [' + cld_sheet + ']: ' + str(repr(e)))
        # log_validation.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Read (special) error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)) + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' CLD_SPECIAL_READ Validation FAILED for ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(
            repr(e)) + '\n')
    return df_spcl_read_dict, read_special_result, error_dict


def cld_map(df_dict, cld_file, error_dict):
    df_map = {}
    map_result, map_desc = 'SUCCESS', 'None'

    # specify standard or exception map set to be used
    if cld_file.CUSTOM_MAP != 'NAN':
        map_base = cld_file.CUSTOM_MAP

    elif cld_file.ADHOC_MAP != 'NAN':
        map_base = cld_file.ADHOC_MAP

    else:
        map_base = cld_file.STATE

    try:

        map_set = map_base + '_' + cld_file.MAG_TYPE + '_MAP'

        for sheet, df in df_dict.items():

            df.columns = df.columns.str.replace('\n', '').str.strip().str.upper()

            # apply map set to df
            if cld_file.MAG_TYPE == 'STD':

                df_mapped = df.rename(columns=state_map_dict[map_set])

            elif cld_file.MAG_TYPE == 'MCO':

                if alt_mag_trigger == 'Y':
                    df_mapped = df.rename(columns=alt_mag_mco_cols)
                else:
                    df_mapped = df.rename(columns=mag_mco_cols)

            elif cld_file.MAG_TYPE == 'FFS':

                if alt_mag_trigger == 'Y':
                    df_mapped = df.rename(columns=alt_mag_ffs_cols)
                else:
                    df_mapped = df.rename(columns=mag_ffs_cols)

            df_map[sheet] = df_mapped

        if bool(df_map) == False:
            map_result, map_desc = 'ERROR_DICT_EMPTY', 'Empty dictionary after initial mapping'

        if 'ERROR' in map_result:
            raise ValueError(map_desc)

        df_map, cld_file, map_result, map_desc, error_dict = cld_map_col_test(df_map, cld_file, map_set, map_result,
                                                                              map_desc, error_dict)

        if 'SUCCESS' in map_result:
            log_validation.write(datetime.strftime(datetime.now(),
                                                   '%m/%d/%Y %H:%M:%S') + ' CLD_MAP Validation Passed for :  ' + cld_file.FILE_NAME + ' [' + sheet + '] ' + '\n')
    except Exception as e:
        map_result, map_desc = 'ERROR', str(repr(e))
        error_dict['map_error'][cld_file.STATE + '_' + cld_file.FILE_NAME] = df
        print('Map error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)))
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' CLD_MAP Validation FAILED with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(
            repr(e)) + '\n')

    return df_map, map_set, map_result, map_desc, error_dict


def cld_map_col_test(df_map, cld_file, map_set, map_result, map_desc, error_dict):
    ### test for mapping gaps ###

    #     possible_req_col_list = list(['NDC_PART_1', 'NDC_PART_2', 'REBATE_QTR_PART_1', 'REBATE_QTR_PART_2', 'NDC11',
    #                                  'ORIGINAL_ICN_TCN', 'INVOICE_QUANTITY', 'NDC', 'CLIENT_PROGRAM_NAME', 'DATE_OF_SERVICE',
    #                                  'ICN', 'ADJUSTED_UNITS'])
    source_col_list = list()

    possible_req_col_list_icn = list(['NDC_PART_1', 'NDC_PART_2', 'NDC11', 'ORIGINAL_ICN_TCN', 'INVOICE_QUANTITY',
                                      'NDC', 'CLIENT_PROGRAM_NAME', 'DATE_OF_SERVICE', 'ICN', 'ADJUSTED_UNITS'])
    possible_req_col_list_no_icn = list(['NDC_PART_1', 'NDC_PART_2', 'NDC11', 'INVOICE_QUANTITY',
                                         'NDC', 'CLIENT_PROGRAM_NAME', 'DATE_OF_SERVICE', 'ADJUSTED_UNITS'])
    # mag_expected_cols = list(['NDC', 'CLIENT_PROGRAM_NAME', 'REBATE_YEAR_QTR', 'DATE_OF_SERVICE', 'ICN', 'ADJUSTED_UNITS'])

    if cld_file.TABS_AS_NDC == 'Y' or cld_file.FILENAME_AS_NDC == 'Y':
        possible_req_col_list_icn.remove('NDC11')
        possible_req_col_list_no_icn.remove('NDC11')
    if cld_file.STATE == 'CA' or cld_file.STATE == 'MT':
        possible_req_col_list_icn.append('PROVIDER_ID_(NPI)')
        possible_req_col_list_no_icn.append('PROVIDER_ID_(NPI)')
    if cld_file.MAG_TYPE == 'STD':
        if 'ORIGINAL_ICN_TCN' in state_map_dict[map_set].values():
            expected_cols = list(set(state_map_dict[map_set].values()) & set(possible_req_col_list_icn))
        else:
            expected_cols = list(set(state_map_dict[map_set].values()) & set(possible_req_col_list_no_icn))
    elif cld_file.MAG_TYPE == 'MCO':
        expected_cols = list(set(mag_mco_cols.values()) & set(possible_req_col_list_icn))
    elif cld_file.MAG_TYPE == 'FFS':
        expected_cols = list(set(mag_ffs_cols.values()) & set(possible_req_col_list_icn))

    try:

        for sheet, df in df_map.items():

            mapped_cols = list(df.columns)
            # print(mapped_cols)
            intersect = set(expected_cols).intersection(set(mapped_cols))
            missing_req_cols = set(expected_cols).symmetric_difference(set(intersect))

            if len(missing_req_cols) > 0:
                missing_col_list = (', '.join(missing_req_cols))
                res = missing_col_list.strip('][').split(', ')

                for column in res:
                    for key, value in state_map_dict[map_set].items():
                        if column == value:
                            raw_cld_field = key.strip('_UP')
                            source_col_list.append(raw_cld_field)
                            # print(source_col_list)
                missing_src_list = (', '.join(source_col_list))
                map_desc = ' Map Issue : Please check for missing fields : ' + missing_src_list + ' in the Raw Cld.'
                # print(map_desc)
                raise ValueError(map_desc)
            if 'SUCCESS' in map_desc:
                log_validation.write(datetime.strftime(datetime.now(),
                                                       '%m/%d/%Y %H:%M:%S') + ' CLD_MAP_COL_TEST Validation Passed for :  ' + cld_file.FILE_NAME + ' [' + sheet + '] ' + '\n')
    except Exception as e:
        map_result = 'MAP_TEST_ERROR'
        map_desc = str(repr(e))
        error_dict['map_error'][cld_file.STATE + '_' + cld_file.FILE_NAME] = df
        # print('Map error (expected column test) with ' + cld_file.STATE + '_' + cld_file.FILE_NAME + ' [' + sheet + '] ' + str(repr(e)))
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' CLD_MAP_COL_TEST Validation FAILED (mandatory column test) with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(
            repr(e)) + '\n')

    return df_map, cld_file, map_result, map_desc, error_dict


def cld_standardize(df_map, cld_file, error_dict):
    df_standardized = {}

    global standardize_result
    global standardize_desc
    df_rbt_file = ""
    df_rbt_in_file = ""

    standardize_result, standardize_desc = 'SUCCESS', 'None'

    try:

        for sheet, df in df_map.items():

            df['STATE'] = cld_file.STATE
            # M&E Sprint 38 changes
            if cld_file.FILE_FORMAT == 'MAG':
                df_rbt_in_file = df['INVOICE YEAR QTR']
                df_rbt_in_file = df_rbt_in_file.str.strip().drop_duplicates()
                df_rbt_file = cld_file.RBT_QTR.replace('Q', '')
                if len(df_rbt_in_file) > 1:
                    standardize_result, standardize_desc = 'ERROR_IN_RBT_QTR_MORE_THAN_ONE', 'Rebate Quarter Issue:Rebate Quarter in the file name does not align with Rebate Quarter in the claims'
                else:
                    df_rbt_in_file = df_rbt_in_file.to_string(index=False).strip()
                    if df_rbt_file != df_rbt_in_file:
                        standardize_result, standardize_desc = 'ERROR_IN_RBT_QTR_NOT_SAME_IN_FILENAME_AND_IN_FILE', 'Rebate Quarter Issue:Rebate Quarter in the file name does not align with Rebate Quarter in the claims'

                    else:

                        df['REBATE_YEAR_QTR'] = cld_file.RBT_QTR  # magellan only col name
            else:
                df['REBATE_YEAR_QTR'] = cld_file.RBT_QTR  #
            df['PROGRAM_ID'] = cld_file.PROG_NAME

            if cld_file.RBT_DT_OVERRIDE == 'NAN' and cld_file.TABS_AS_RBT_QTR == 'NAN':
                df['REBATE_QUARTER'] = cld_file.RBT_QTR

            # if invoice quantity column is inconsistent this allows identification of 2 columns and preference
            if {'INVOICE_QUANTITY_PREFFERED', 'INVOICE_QUANTITY_SECONDARY'}.issubset(df.columns):
                df['INVOICE_QUANTITY'] = df.INVOICE_QUANTITY_PREFFERED.combine_first(df.INVOICE_QUANTITY_SECONDARY)
            elif 'INVOICE_QUANTITY_PREFFERED' in df.columns:
                df['INVOICE_QUANTITY'] = df['INVOICE_QUANTITY_PREFFERED']
            elif 'INVOICE_QUANTITY_SECONDARY' in df.columns:
                df['INVOICE_QUANTITY'] = df['INVOICE_QUANTITY_SECONDARY']

            # if provider quantity column is inconsistent this allows identification of 2 columns and preference
            if {'PROVIDER_QUANTITY_PREFFERED', 'PROVIDER_QUANTITY_SECONDARY'}.issubset(df.columns):
                df['PROVIDER_QUANTITY'] = df.PROVIDER_QUANTITY_PREFFERED.combine_first(df.PROVIDER_QUANTITY_SECONDARY)
            elif 'PROVIDER_QUANTITY_PREFFERED' in df.columns:
                df['PROVIDER_QUANTITY'] = df['PROVIDER_QUANTITY_PREFFERED']
            elif 'PROVIDER_QUANTITY_SECONDARY' in df.columns:
                df['PROVIDER_QUANTITY'] = df['PROVIDER_QUANTITY_SECONDARY']

            # if
            # df['PROVIDER_QUANTITY'] = df['PROVIDER_QUANTITY_SECONDARY']

            if 'NDC_PART_1' in df.columns:  # combine multi-column NDC values by including NDC_PART_1 in mapping file

                if 'NDC_PART_3' in df.columns:
                    df['NDC11'] = df['NDC_PART_1'] + df['NDC_PART_2'] + df['NDC_PART_3']

                else:
                    df['NDC11'] = df['NDC_PART_1'] + df['NDC_PART_2']

            if 'REBATE_QTR_PART_1' in df.columns:  # combine multi-column rebate quarter values by including REBATE_QTR_PART_1 in mapping file,
                # use in conjunction with RBT_DT_OVERRIDE config to standardize values

                df['REBATE_QUARTER'] = df['REBATE_QTR_PART_1'] + df['REBATE_QTR_PART_2']

            if cld_file.TABS_AS_RBT_QTR == 'Y':
                rebate_tab_assess_df = pd.DataFrame({"FILE_NAME": [sheet], "FILE_PATH": [cld_file.FILE_PATH]})
                tab_assess_rbt_qtr = rebate_tab_assess_df.apply(lambda x: qtr_assess(x['FILE_NAME'], x['FILE_PATH']),
                                                                axis=1)
                tab_rbt_qtr = tab_assess_rbt_qtr[0]
                df['REBATE_QUARTER'] = tab_rbt_qtr

            if cld_file.TABS_AS_NDC == 'Y':
                df['NDC11'] = df.apply(lambda x: ndc_assess(str(sheet), cld_file.LABELER_NAME, cld_file.FILE_PATH),
                                       axis=1)

            if cld_file.FILENAME_AS_NDC == 'Y':
                df['NDC11'] = cld_file.NDC

            if cld_file.PARSE_NPI == 'Y' and 'PROVIDER_ID_(NPI)' in df.columns:
                df['PROVIDER_ID_(NPI)'] = df['PROVIDER_ID_(NPI)'].apply(parse_col_npi)

            if cld_file.STATE == 'CA':
                df['RX_ID'] = df['RX_ID'].str.replace('?', '')  # remove filler data
                df['PROVIDER_QUANTITY'] = df[
                    'INVOICE_QUANTITY_SECONDARY']  # Map 'INVOICE_QUANTITY_SECONDARY' as 'PROVIDER QUANTITY'

            ### limit dataframe with configured column ###

            if cld_file.LIMIT_ON == 'NDC_PARSE_LIMIT':  # set this value in LIMIT_ON config to parse NDC as a df limit
                df['NDC_PARSE_LIMIT'] = df.apply(
                    lambda x: ndc_assess(x['NDC11'], cld_file.LABELER_NAME, cld_file.FILE_PATH), axis=1)
                df = df[df['NDC_PARSE_LIMIT'] != 'UNK']
                df = df[~df['NDC_PARSE_LIMIT'].isnull()]
                df['NDC11'] = df['NDC_PARSE_LIMIT']

            elif cld_file.LIMIT_ON != 'NAN':
                df = df[~df[cld_file.LIMIT_ON].isnull()]

            else:
                df = df[~df['DATE_OF_SERVICE'].isnull()]

            if cld_file.FILE_FORMAT == 'STD':
                df['NDC11'] = df['NDC11'].str.replace('-', '')  # remove NDC dashes
                df['NDC11'] = df['NDC11'].str.replace('[^\x00-\x7F]', '')  # remove NDC junk

            df_standardized[sheet] = df
        if run_parameter == 'CONVERTER':
            if cld_file.USE_CONVERT_FILE == 'Y' or cld_file.CONVERSION_EXCEPT == 'Y':
                df_standardized, convert_result, error_dict = cld_unit_convert(df_standardized, cld_file, error_dict)
                standardize_result = convert_result

        if bool(df_standardized) == False:
            standardize_result, standardize_desc = 'ERROR_DICT_EMPTY', 'Empty dictionary after standardize'

        if 'ERROR' in standardize_result:
            raise ValueError(standardize_desc)

        if 'SUCCESS' in standardize_result:
            log_validation.write(datetime.strftime(datetime.now(),
                                                   '%m/%d/%Y %H:%M:%S') + ' CLD_STANDARIZE Validation Passed with ' + cld_file.FILE_NAME + ' [' + sheet + '] ' + '\n')
    except Exception as e:
        standardize_result = 'ERROR'
        error_dict['standardize_error'][cld_file.STATE + '_' + cld_file.FILE_NAME] = df
        print('Standardize error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)))
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' CLD_STANDARIZE Validation FAILED with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(
            repr(e)) + '\n')
        # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Standardize error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)) + '\n')

    return df_standardized, standardize_result, standardize_desc, error_dict


# In[64]:


def cld_unit_convert(df_standardized, cld_file, error_dict):
    ### apply unit conversions ###
    converted_standardized_dict = {}
    convert_result = 'SUCCESS'

    try:

        for sheet, df in df_standardized.items():

            if cld_file.USE_CONVERT_FILE == 'Y':

                if cld_file.CONVERSION_EXCEPT == 'Y':
                    print(''' You shouldn't be here, setup configs properly''')

                else:

                    df = pd.merge(df, convert_factor, left_on=['STATE', 'NDC11'],
                                  right_on=['STATE', 'NDC'], how='left')

                df = df.rename(columns={'INVOICE_QUANTITY': 'INVOICE_QUANTITY_RAW'})
                df['INVOICE_QUANTITY_RAW'] = df['INVOICE_QUANTITY_RAW'].astype(float)

                df['INVOICE_QUANTITY'] = df.apply(lambda x: unit_convert(x['INVOICE_QUANTITY_RAW'],
                                                                         x['FINAL_CF'],
                                                                         x['OPERATOR']), axis=1)

                converted_standardized_dict[sheet] = df

            if cld_file.USE_CONVERT_FILE != 'Y' and cld_file.CONVERSION_EXCEPT == 'Y':

                current_file_config = []
                ndc_convert_eval_headers = {}

                current_file_config = pd.DataFrame(cld_file).T
                current_file_config = current_file_config.drop(0, axis=1)
                current_file_config.columns = config_table.columns

                current_file_config = current_file_config[['STATE', 'PROG_NAME', 'LABELER_NAME', 'INVC_QTR', 'RBT_QTR']]
                iter_plus = 0
                iter_min = 0

                for row in range(cf_exceptions_ndc_lvl.shape[0]):

                    convert_exception = []

                    ndc_convert_eval_headers[row] = cf_exceptions_ndc_lvl.iloc[[row]].dropna(axis=1)
                    convert_exception = ndc_convert_eval_headers[row]

                    convert_eval_join_values = list(ndc_convert_eval_headers[row])
                    convert_eval_join_values = [x for x in convert_eval_join_values if
                                                x not in ['CONVERSION_EXCEPT', 'NDC_DROP', 'EXCEPT_TYPE']]

                    current_file_config = pd.merge(current_file_config, convert_exception, on=convert_eval_join_values,
                                                   how='left')

                    if 'NDC_DROP_y' in current_file_config.columns:
                        current_file_config.rename(columns={'NDC_DROP_y': 'NDC_DROP_' + str(iter_plus),
                                                            'EXCEPT_TYPE_y': 'EXCEPT_TYPE_' + str(iter_plus)},
                                                   inplace=True)
                        current_file_config.rename(columns={'NDC_DROP_x': 'NDC_DROP_' + str(iter_min),
                                                            'EXCEPT_TYPE_x': 'EXCEPT_TYPE_' + str(iter_min)},
                                                   inplace=True)
                        iter_plus = iter_plus + 1
                        iter_min = iter_min - 1

                convert_eval_cols = [col for col in current_file_config.columns if
                                     ('NDC_DROP' in col) or ('EXCEPT_TYPE' in col)]
                ndc_exception = current_file_config[convert_eval_cols]

                ndc_except_df = pd.DataFrame(list(ndc_exception.values.astype(str))).T
                ndc_except_df.columns = ['NDC']
                ndc_except_df = ndc_except_df.loc[ndc_except_df['NDC'] != 'nan']

                ndc_except_type_df = ndc_except_df.copy()
                ndc_except_type_df = ndc_except_type_df.reset_index(drop=True)
                ndc_except_type_df['EXCEPT_TYPE'] = ''

                for i in range(ndc_except_type_df.shape[0]):
                    if i < ndc_except_type_df.shape[0] - 1:
                        ndc_except_type_df['EXCEPT_TYPE'].iloc[i] = ndc_except_type_df['NDC'].iloc[i + 1]

                ndc_except_type_df = ndc_except_type_df[
                    (ndc_except_type_df.NDC != 'CONVERT') & (ndc_except_type_df.NDC != 'EXCLUDE')].drop_duplicates()
                ndc_except_df = ndc_except_type_df.copy()

                convert_factor_except_list = convert_factor.copy()
                convert_factor_except_list = pd.merge(convert_factor_except_list, ndc_except_df, on='NDC', how='left')
                convert_factor_except_list = convert_factor_except_list.loc[
                    convert_factor_except_list['EXCEPT_TYPE'] != 'EXCLUDE']

                if len(convert_factor_except_list.loc[convert_factor_except_list['EXCEPT_TYPE'] == 'CONVERT']) > 0:
                    convert_factor_except_list = convert_factor_except_list.loc[
                        convert_factor_except_list['EXCEPT_TYPE'] == 'CONVERT']

                df = pd.merge(df, convert_factor_except_list, left_on=['STATE', 'NDC11'],
                              right_on=['STATE', 'NDC'], how='left')

                df.rename(columns={'INVOICE_QUANTITY': 'INVOICE_QUANTITY_RAW'}, inplace=True)
                df['INVOICE_QUANTITY_RAW'] = df['INVOICE_QUANTITY_RAW'].astype(float)

                df['INVOICE_QUANTITY'] = df.apply(lambda x: unit_convert(x['INVOICE_QUANTITY_RAW'],
                                                                         x['FINAL_CF'],
                                                                         x['OPERATOR']), axis=1)

                converted_standardized_dict[sheet] = df

        if bool(converted_standardized_dict) == False:
            convert_result, convert_desc = 'ERROR_DICT_EMPTY', 'Empty dictionary after conversion'

        if 'ERROR' in standardize_result:
            raise ValueError(convert_desc)

    except Exception as e:
        convert_result = 'CONVERSION_ERROR'
        error_dict['standardize_error'][cld_file.STATE + '_' + cld_file.FILE_NAME] = df
        print('Standardize (conversion) error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)))
        # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Standardize (conversion) error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)) + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' Standardize (conversion) error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(
            repr(e)) + '\n')
    return converted_standardized_dict, convert_result, error_dict


def cld_finalize(df_standardize_dict, cld_file, error_dict):
    df_finalized = {}
    finalize_result, finalize_desc = "SUCCESS", 'None'
    file_output_name = 'error'

    ### reindex dataframe with standard or magellan mappings ###
    try:

        for sheet, df in df_standardize_dict.items():

            if cld_file.FILE_FORMAT == 'STD':

                df_final = df.reindex(std_file_cols, axis='columns', fill_value=None)
                file_output_name = cld_file.FILE_FORMAT + '_' + cld_file.STATE + '_' + cld_file.LABELER_NAME + '_' + cld_file.PROG_NAME + '_' + cld_file.INVC_QTR
                file_output_name = file_output_name.replace(" ", "_")

                if cld_file.INV_DT_OVERRIDE != 'NAN':  # use and standardize invoice quarter in file (override directory input)
                    df_final['INVOICE_QUARTER'] = df_final.apply(
                        lambda x: qtr_assess(x['INVOICE_QUARTER'], cld_file.FILE_PATH), axis=1)
                else:
                    df_final['INVOICE_QUARTER'] = cld_file.INVC_QTR

                if cld_file.RBT_DT_OVERRIDE != 'NAN':  # use and standardize rebate quarter in file (override directory input)

                    if cld_file.RBT_DT_OVERRIDE == 'CONVERT_DATE':  # convert to quarter from date
                        df_final.REBATE_QUARTER = pd.to_datetime(df_final.REBATE_QUARTER)
                        df_final['REBATE_QUARTER'] = pd.PeriodIndex(df_final.REBATE_QUARTER, freq='Q')
                    else:
                        df_final['REBATE_QUARTER'] = df_final.apply(
                            lambda x: qtr_assess(x['REBATE_QUARTER'], cld_file.FILE_PATH), axis=1)


            elif cld_file.FILE_FORMAT == 'MAG':

                file_output_name = cld_file.FILE_FORMAT + '_' + cld_file.STATE + '_' + cld_file.LABELER_NAME + '_' + cld_file.MAG_TYPE + '_' + cld_file.PROG_NAME + '_' + cld_file.INVC_QTR
                file_output_name = file_output_name.replace(" ", "_")

                if cld_file.MAG_TYPE == 'MCO':
                    df_final = df.reindex(mag_mco_file_cols, axis='columns', fill_value=None)
                elif cld_file.MAG_TYPE == 'FFS':
                    df_final = df.reindex(mag_ffs_file_cols, axis='columns', fill_value=None)

                df_final = df_final.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # remove whitespace

            ### apply final post-index standardizations ###

            df_final['DATE_OF_SERVICE'] = pd.to_datetime(df_final['DATE_OF_SERVICE']).dt.strftime("%Y%m%d")
            df_final['PAID_DATE'] = pd.to_datetime(df_final['PAID_DATE']).dt.strftime("%Y%m%d")
            df_final['PAID_DATE'] = df_final['PAID_DATE'].str.replace('NaT', '')

            dollar_str_cols = ['BILLED_AMOUNT', 'MEDICAID_REIMBURSEMENT_AMOUNT',
                               'NON_MEDICAID_REIMBURSEMENT_AMOUNT_(TPL)', 'MEDICAID_AMOUNT_REIMBURSED',
                               'NON_MEDICAID_AMOUNT_REIMBURSED']

            mapped_dtypes = df_final.dtypes
            mapped_str_dtypes = mapped_dtypes[mapped_dtypes != 'float64']

            convert_cols = [x for x in dollar_str_cols if x in mapped_str_dtypes]

            if cld_file.STATE != 'OR':  # remove string dollar values
                df_final[convert_cols] = df_final[convert_cols].apply(
                    lambda x: x.str.replace(',', '').str.replace('(', '-').str.replace(')', '').str.replace('$', ''))

            df_finalized[sheet] = df_final

        if bool(df_finalized) == False:
            finalize_result, finalize_desc = 'ERROR_DICT_EMPTY', 'Empty dictionary after conversion'

        if 'ERROR' in finalize_result:
            raise ValueError(finalize_desc)
        if 'SUCCESS' in finalize_result:
            log_validation.write(datetime.strftime(datetime.now(),
                                                   '%m/%d/%Y %H:%M:%S') + ' CLD_FINALIZE passed  with ' + cld_file.FILE_NAME + ' [' + sheet + '] ' + '\n')
    except Exception as e:
        finalize_result = "ERROR"
        error_dict['finalize_error'][cld_file.STATE + ' ' + cld_file.FILE_NAME] = df_final
        print('Finalize error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)))
        if (finalize_desc == 'None'):
            finalize_desc = ' [' + sheet + ']: ' + str(repr(e))
        # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Finalize error with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(repr(e)) + '\n')
        log_validation.write(datetime.strftime(datetime.now(),
                                               '%m/%d/%Y %H:%M:%S') + ' CLD_FINALIZE validation failed with ' + cld_file.FILE_NAME + ' [' + sheet + ']: ' + str(
            repr(e)) + '\n')
    return df_finalized, file_output_name, finalize_result, finalize_desc, error_dict


def cld_test(df_finalize_dict, map_set, cld_file, error_dict):
    cld_test_result, test_desc = 'SUCCESS', 'None'

    for sheet, df in df_finalize_dict.items():

        ## null column test ##
        null_cols_test = df.isnull().any()
        possible_req_col_list_icn = list(
            ['PROGRAM_ID', 'INVOICE_QUARTER', 'REBATE_QUARTER', 'DATE_OF_SERVICE', 'NDC11', 'INVOICE_QUANTITY',
             'NDC', 'CLIENT_PROGRAM_NAME', 'REBATE_YEAR_QTR', 'ICN', 'ADJUSTED_UNITS', 'ORIGINAL_ICN_TCN'])
        possible_req_col_list_no_icn = list(
            ['PROGRAM_ID', 'INVOICE_QUARTER', 'REBATE_QUARTER', 'DATE_OF_SERVICE', 'NDC11', 'INVOICE_QUANTITY',
             'NDC', 'CLIENT_PROGRAM_NAME', 'REBATE_YEAR_QTR', 'ADJUSTED_UNITS'])
        if cld_file.MAG_TYPE == 'STD':
            if 'ORIGINAL_ICN_TCN' in state_map_dict[map_set].values():
                expected_cols = list(set(state_map_dict[map_set].values()) & set(possible_req_col_list_icn))
            else:
                expected_cols = list(set(state_map_dict[map_set].values()) & set(possible_req_col_list_no_icn))
        else:
            expected_cols = list(set(df.columns.values) & set(possible_req_col_list_icn))

        null_cols_test = null_cols_test[expected_cols]

        for idx, val in zip(null_cols_test.index, null_cols_test):

            if val == True:
                cld_test_result = 'NULL_VALUE_TEST_ERROR'
                error_dict['test_error'][cld_file.STATE + '_' + cld_file.FILE_NAME] = df
                test_desc = 'Null value Issue : Empty cell found with Sheet ' + ' [' + sheet + '] for column: ' + idx
                print(test_desc)
                # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Test error (null value test) with ' + cld_file.FILE_NAME + ' [' + sheet + '] for column: ' + idx + '\n')
                log_validation.write(datetime.strftime(datetime.now(),
                                                       '%m/%d/%Y %H:%M:%S') + ' Test error (null value test) with ' + cld_file.FILE_NAME + ' [' + sheet + '] for column: ' + idx + '\n')
        ## UNK value test ##

        if cld_file.MAG_TYPE == 'STD':

            unk_df = df.isin({'NDC11': ['UNK'], 'REBATE_QUARTER': ['UNK'], 'INVOICE_QUARTER': ['UNK']})

            for idx, val in zip(unk_df, unk_df.any()):

                if val == True:
                    cld_test_result, test_desc = 'UNK_VALUE_TEST_ERROR', 'Test error (unknown value test) with ' + cld_file.FILE_NAME + ' [' + sheet + '] for column: ' + idx
                    error_dict['test_error'][cld_file.STATE + '_' + cld_file.FILE_NAME] = df
                    print(test_desc)
                    # log_error.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Test error (unknown value test) with ' + cld_file.FILE_NAME + ' [' + sheet + '] for column: ' + idx + '\n')
                    log_validation.write(datetime.strftime(datetime.now(),
                                                           '%m/%d/%Y %H:%M:%S') + ' CLD_TEST Validation FAILED (unknown value test) with ' + cld_file.FILE_NAME + ' [' + sheet + '] for column: ' + idx + '\n')
    return cld_test_result, test_desc, error_dict


def cld_write(df_finalize_dict, file_output_name):
    write_result, write_desc = 'SUCCESS', 'None'

    if bool(df_finalize_dict) == False:
        write_result = 'ERROR_DICT_EMPTY'

    else:

        try:

            for sheet, df in df_finalize_dict.items():

                if not os.path.isfile(curr_dir + '/outputs/process_working/' + file_output_name + '.csv'):
                    df.to_csv(curr_dir + '/outputs/process_working/' + file_output_name + '.csv', index=False)

                else:
                    df.to_csv(curr_dir + '/outputs/process_working/' + file_output_name + '.csv', index=False, mode='a',
                              header=False)

                print(
                    'Processed file: ' + cld_file.FILE_NAME + ' [' + sheet + ']' + '  ->   ' + file_output_name + '.csv')
                log_success.write(datetime.strftime(datetime.now(),
                                                    '%m/%d/%Y %H:%M:%S') + ' Processed file ' + cld_file.FILE_PATH + ' [' + sheet + ']' + '  ->   ' + file_output_name + '.csv' '\n')

            archive_directory = cld_file.DIR_PATH + '/_archived/'
            new_archived_name = datetime.strftime(datetime.now(), '%m_%d_%Y_%H_%M_%S' + '_' + cld_file.FILE_NAME)
            archive_name = cld_file.DIR_PATH + '/' + new_archived_name

            cwd = os.getcwd()
            old_file = os.path.join(cld_file.DIR_PATH, cld_file.FILE_NAME)
            new_file = os.path.join(cld_file.DIR_PATH, new_archived_name)
            os.chdir(cld_file.DIR_PATH)
            os.rename(cld_file.FILE_NAME, new_archived_name)
            os.chdir(cwd)

            if not os.path.exists(archive_directory):
                os.makedirs(archive_directory)
            try:

                shutil.move(archive_name, archive_directory)
                log_success.write(datetime.strftime(datetime.now(),
                                                    '%m-%d-%Y %H:%M:%S') + ' Archiving file ' + cld_file.FILE_NAME + ' to ' + archive_directory + '\n' + '\n')
                log_validation.write(datetime.strftime(datetime.now(),
                                                       '%m-%d-%Y %H:%M:%S') + ' Archiving file ' + cld_file.FILE_NAME + ' to ' + archive_directory + '\n' + '\n')
                print('Archived ' + cld_file.FILE_NAME)

            except Exception as e:
                write_result, write_desc = 'ARCHIVE_ERROR', 'Write error trying to move file ' + cld_file.FILE_NAME + ' ' + str(
                    repr(e))
                print(write_desc)
                log_validation.write(datetime.strftime(datetime.now(),
                                                       '%m/%d/%Y %H:%M:%S') + ' Write error trying to move file with ' + archive_name + ' to ' + archive_directory + '\n')

        except Exception as e:
            write_result, write_desc = 'ERROR', 'Write error (general) with file ' + cld_file.FILE_NAME + ' ' + str(
                repr(e))
            print(write_desc)
            log_validation.write(datetime.strftime(datetime.now(),
                                                   '%m/%d/%Y %H:%M:%S') + ' Write error (general) with file ' + cld_file.FILE_NAME + '\n')

    return write_result, write_desc


### process configured files ###

cld_summary_cols = list(config_table.columns.values)
cld_summary_cols.extend(
    ['READ_RESULT', 'MAP_RESULT', 'STANDARDIZE_RESULT', 'FINALIZE_RESULT', 'CLD_TEST_RESULT', 'WRITE_RESULT'])
cld_run_summary_build = pd.DataFrame(columns=cld_summary_cols)
cld_validation_success = pd.DataFrame(columns=cld_summary_cols)
existing_process_files = glob.glob(
    curr_dir + '/outputs/process_working/*.*')  # remove existing files from temporary process folder
for f in existing_process_files:
    os.remove(f)

error_dict = {}
error_dict['read_error'] = {}
error_dict['map_error'] = {}
error_dict['standardize_error'] = {}
error_dict['finalize_error'] = {}
error_dict['test_error'] = {}

# print excluded files


for excluded_file in error_files.itertuples():
    # error_files['STATE'] = error_files['STATE'].fillna('?')
    print(
        excluded_file.STATE + ' ' + excluded_file.FILE_NAME + ' is being excluded from run because: ' + excluded_file.EXCLUDE_DESCRIP)

for cld_file in config_table_all.itertuples():
    log_validation.write(
        '\n' + 'Process started for ' + ' : ' + cld_file.PROG_NAME + '-' + cld_file.LABELER_NAME + '\n')
    current_cld_file = pd.DataFrame(cld_file).transpose().drop(0, axis=1)

    current_cld_file.columns = list(config_table.columns.values)
    current_cld_file['READ_RESULT'], current_cld_file['MAP_RESULT'], current_cld_file['STANDARDIZE_RESULT'], \
    current_cld_file['FINALIZE_RESULT'], current_cld_file['CLD_TEST_RESULT'], current_cld_file['WRITE_RESULT'] = [
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]

    # check if file is configured to run
    if cld_file.EXCLUDE_FILE == 'Y':
        cld_run_summary_build = cld_run_summary_build.append(current_cld_file)
        log_validation.write(
            excluded_file.STATE + ' ' + excluded_file.FILE_NAME + ' is being excluded from run because: ' + excluded_file.EXCLUDE_DESCRIP + '\n')
        continue

    # read
    df_read_dict, alt_mag_trigger, read_result, read_error_descrip, error_dict = cld_read(cld_file, error_dict)

    current_cld_file['READ_RESULT'], current_cld_file['EXCLUDE_DESCRIP'] = read_result, read_error_descrip
    if 'ERROR' in read_result:
        if 'Unsupported format, or corrupt file' in read_error_descrip:
            read_error_descrip = "Unsupported format, or corrupt file :Error reading File."
            current_cld_file['EXCLUDE_DESCRIP'] = read_error_descrip
        if "TypeError('sequence item 1: expected string, float found',)" in read_error_descrip:
            read_error_descrip = "Header not found at Expected row :Error reading File."
            current_cld_file['EXCLUDE_DESCRIP'] = read_error_descrip
        if 'XLRDError("Can\'t find workbook in OLE2 compound document")' in read_error_descrip:
            read_error_descrip = "Read Issue :Error Opening Workbook ,File might be password protected."
            current_cld_file['EXCLUDE_DESCRIP'] = read_error_descrip
        cld_run_summary_build = cld_run_summary_build.append(current_cld_file)
        error_files = error_files.append((add_status_issue(cld_file, read_error_descrip)))
        continue

    # map
    df_map_dict, map_set, map_result, map_desc, error_dict = cld_map(df_read_dict, cld_file, error_dict)

    current_cld_file['MAP_RESULT'], current_cld_file['EXCLUDE_DESCRIP'] = map_result, map_desc
    if 'ERROR' in map_result:
        cld_run_summary_build = cld_run_summary_build.append(current_cld_file)
        error_files = error_files.append((add_status_issue(cld_file, map_desc)))
        continue

    # standardize
    df_standardize_dict, standardize_result, standardize_desc, error_dict = cld_standardize(df_map_dict, cld_file,
                                                                                            error_dict)

    current_cld_file['STANDARDIZE_RESULT'], current_cld_file['EXCLUDE_DESCRIP'] = standardize_result, standardize_desc
    if 'ERROR' in standardize_result:
        cld_run_summary_build = cld_run_summary_build.append(current_cld_file)
        error_files = error_files.append((add_status_issue(cld_file, standardize_desc)))
        continue

    # finalize
    df_finalize_dict, file_output_name, finalize_result, finalize_desc, error_dict = cld_finalize(df_standardize_dict,
                                                                                                  cld_file, error_dict)

    current_cld_file['FINALIZE_RESULT'], current_cld_file['EXCLUDE_DESCRIP'] = finalize_result, finalize_desc
    if 'ERROR' in finalize_result:
        if "'year is out of range'" in finalize_desc:
            finalize_desc = 'Service Date out of Range for Tab' + finalize_desc.strip(
                "ParserError(u'year is out of range: %s'")
            current_cld_file['EXCLUDE_DESCRIP'] = finalize_desc
        if "ValueError('Given date string not likely a datetime" in finalize_desc:
            current_cld_file['EXCLUDE_DESCRIP'] = 'Date format Issue for Tab' + finalize_desc
        else:
            current_cld_file['EXCLUDE_DESCRIP'] = 'Issue with Data for Tab:' + finalize_desc
        cld_run_summary_build = cld_run_summary_build.append(current_cld_file)
        error_files = error_files.append((add_status_issue(cld_file, finalize_desc)))
        continue

    # test
    cld_test_result, test_desc, error_dict = cld_test(df_finalize_dict, map_set, cld_file, error_dict)

    current_cld_file['CLD_TEST_RESULT'], current_cld_file['EXCLUDE_DESCRIP'] = cld_test_result, test_desc
    if 'ERROR' in cld_test_result:
        cld_run_summary_build = cld_run_summary_build.append(current_cld_file)
        error_files = error_files.append((add_status_issue(cld_file, test_desc)))
        continue

    # write
    if run_parameter == 'CONVERTER':
        write_result, write_desc = cld_write(df_finalize_dict, file_output_name)

        current_cld_file['WRITE_RESULT'] = write_result
        if 'ERROR' in write_result:
            cld_run_summary_build = cld_run_summary_build.append(current_cld_file)
            error_files = error_files.append((add_status_issue(cld_file, write_desc)))
            continue

    cld_run_summary_build = cld_run_summary_build.append(current_cld_file)

# In[69]:


### write result summary tables ###

if len(cld_run_summary_build) > 0:

    try:

        cld_run_summary_full = cld_run_summary_build.copy()
        cld_validation = cld_run_summary_full[['STATE', 'FILE_NAME', 'EXCLUDE_DESCRIP']].copy()
        cld_validation = cld_validation[cld_validation.EXCLUDE_DESCRIP != 'None']
        cld_validation.rename(columns={'STATE': 'STATE', 'FILE_NAME': 'FILE', 'EXCLUDE_DESCRIP': 'ISSUE_DESCRIPTION'},
                              inplace=True)

        cld_run_summary_full['RUN_DATE'] = pd.datetime.now().strftime("%m/%d/%Y %I:%M:%S")

        cld_run_summary = cld_run_summary_full[
            ['RUN_DATE', 'DIR_PATH', 'FILE_NAME', 'ACTIVE_CONFIG', 'STATE', 'EXCLUDE_FILE',
             'READ_RESULT', 'MAP_RESULT', 'STANDARDIZE_RESULT', 'FINALIZE_RESULT',
             'CLD_TEST_RESULT', 'WRITE_RESULT', 'EXCLUDE_DESCRIP']]

        cld_run_summary_full.to_excel(curr_dir + '/temp/last_run_summary_full.xlsx', index=False)
        cld_run_summary.to_excel(curr_dir + '/temp/last_run_summary.xlsx', index=False)
        cld_validation_success = cld_run_summary[cld_run_summary.EXCLUDE_DESCRIP == 'None']
        cld_validation_success = cld_validation_success[['STATE', 'FILE_NAME']]
        if (run_parameter == 'CONVERTER'):

            if not os.path.isfile(curr_dir + '/outputs/logs/' + process_qtr + '_summary_full.csv'):
                cld_run_summary_full.to_csv(curr_dir + '/outputs/logs/' + process_qtr + '_summary_full.csv'
                                            , index=False)

            else:
                cld_run_summary_full.to_csv(curr_dir + '/outputs/logs/' + process_qtr + '_summary_full.csv'
                                            , index=False
                                            , mode='a'
                                            , header=False)

            if not os.path.isfile(curr_dir + '/outputs/logs/' + process_qtr + '_summary.csv'):
                cld_run_summary.to_csv(curr_dir + '/outputs/logs/' + process_qtr + '_summary.csv'
                                       , index=False)

            else:
                cld_run_summary.to_csv(curr_dir + '/outputs/logs/' + process_qtr + '_summary.csv'
                                       , index=False
                                       , mode='a'
                                       , header=False)
        if not os.path.isfile(curr_dir + '/outputs/logs/' + process_qtr + '_cld_validation.csv'):
            cld_validation.to_csv(curr_dir + '/outputs/logs/' + process_qtr + '_cld_validation.csv'
                                  , index=False)
        else:
            cld_validation.to_csv(curr_dir + '/outputs/logs/' + process_qtr + '_cld_validation.csv'
                                  , index=False)

    except Exception as e:
        print(e)

# In[70]:


### move final files to inbound dir ###
processing_dir = "/NAS/SADMIN/cdip/DEV/MDI/CDIP/scripts/MDI-Preprocess/outputs/process_working/"
processed_dir = "/NAS/SADMIN/cdip/DEV/MDI/CDIP/SrcFiles/CLD_INBOUND/"

# processing_dir = "/NAS/SADMIN/cdip/PROD/MDI/CDIP/scripts/MDI-Preprocess/outputs/process_working/" --
# processed_dir = "/NAS/SADMIN/cdip/PROD/MDI/CDIP/SrcFiles/CLD_INBOUND/" --
# processed_dir = '\\\\dnafiles2\sadmin2\cdip\DEV\MDI\CDIP\SrcFiles\CLD_INBOUND\'
# processing_dir = curr_dir+'/outputs/process_working/'
# processed_dir = curr_dir+'/outputs/processed/'
processed_files = os.listdir(processing_dir)

if run_parameter == 'CONVERTER':
    for f in processed_files:

        try:
            shutil.move(processing_dir + f, processed_dir)
            log_success.write(datetime.strftime(datetime.now(),
                                                '%m/%d/%Y %H:%M:%S') + ' Moving file ' + f + ' to target ' + processed_dir + '\n')
            # log_validation.write(datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S') + ' Moving file ' + f + ' to target ' + processed_dir + '\n')
            print('Moving ' + f)

        except Exception as e:
            print(e)
            continue

### Validation Status email###
if run_parameter == 'VALIDATOR' or run_parameter == 'CONVERTER':
    validation_status_email()

### clean up ###

# log_error.close()
log_validation.close()
if (run_parameter == 'CONVERTER'):
    log_success.close()








