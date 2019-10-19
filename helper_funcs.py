from datetime import datetime, date

def organise_output(contents):
    list_contents = list(contents)
    for i, d in enumerate(list_contents):
        line = '|'.join(str(item).ljust(80) for item in d)
        if i == 0:
            print('-' * len(line))
        print(line)

def convert_to_date(date_string):
    strip_hyphen = ' '.join(date_string.split('-'))
    converted_date = datetime.strptime(strip_hyphen, "%d %b %y").date()
    return converted_date

def format_date(date_object):
    formatted_date = date_object.strftime('%d/%m/%Y')
    return formatted_date