import csv
from operator import itemgetter
from collections import defaultdict
from datetime import datetime, date

import helper_funcs

with open('Mobile Phone Masts 01.04.2019a.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    list_masts = list(csv_reader)
    headers = list_masts.pop(0)
sorted_masts = sorted(list_masts, key = itemgetter(9))

def get_first_5_items():
    first_5_items = [sorted_masts[index] for index in range(5)]
    helper_funcs.organise_output([headers])
    helper_funcs.organise_output(first_5_items)

def get_data_lease_25_yrs():
    lease_25_yrs = [item for item in sorted_masts if item[7] == '25']
    helper_funcs.organise_output([headers])
    helper_funcs.organise_output(lease_25_yrs)
    total_rent = 0
    for item in lease_25_yrs:
        total_rent += float(item[9])
    print('Total rent for all items is ' + str(total_rent))
    
def dict_tenant_and_mast():
    dict = defaultdict(int)
    for item in list_masts:
        dict[item[2]] += 1
    dict_list = []
    for key, value in dict.items():
        dict_list.append([key, value])
    helper_funcs.organise_output([['Tenant name', 'Count of masts']])
    helper_funcs.organise_output(dict_list)

def lease_between_99_and_07():
    list_data = []
    for item in list_masts:
        try:
            lease_start_date = helper_funcs.convert_to_date(item[5])
            if date(1999, 6, 1) <= lease_start_date <= date(2007, 8, 31):
                item[5] = helper_funcs.format_date(lease_start_date)
                try:
                    lease_end_date = helper_funcs.convert_to_date(item[6])
                    item[6] = helper_funcs.format_date(lease_end_date)
                except:
                    pass
                try:
                    next_rent_review = helper_funcs.convert_to_date(item[8])
                    item[8] = helper_funcs.format_date(next_rent_review)
                except:
                    pass
                list_data.append(item)
        except:
            continue
    helper_funcs.organise_output([headers])
    helper_funcs.organise_output(list_data)

def run_all():
    get_first_5_items()
    get_data_lease_25_yrs()
    dict_tenant_and_mast()
    lease_between_99_and_07()