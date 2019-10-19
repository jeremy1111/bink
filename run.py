import main_code

func_dict = {'Get first five items' : main_code.get_first_5_items,
             'Get data where lease years is 25' : main_code.get_data_lease_25_yrs,
             'Get tenant name and count of masts' : main_code.dict_tenant_and_mast,
             'Get rentals between 01/06/1999 and 31/08/2007' : main_code.lease_between_99_and_07,
             'Run everything' : main_code.run_all
             }

if __name__ == '__main__':
    input('Press enter to begin')
    command = input('> ')
    func_dict[command]()