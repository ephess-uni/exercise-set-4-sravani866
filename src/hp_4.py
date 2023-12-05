


from datetime import datetime, timedelta
import csv
from collections import defaultdict

def reformat_dates(dates):
    """
    Reformat a list of date strings from 'yyyy-mm-dd' to 'dd mmm yyyy'.
    
    Parameters:
    - dates (list): A list of date strings in the format 'yyyy-mm-dd'.
    
    Returns:
    - list: A list of reformatted date strings in the format 'dd mmm yyyy'.
    """
    reformatted_dates = []
    for date_str in dates:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        reformatted_dates.append(date_obj.strftime('%d %b %Y'))
    return reformatted_dates



def date_range(start, n):
    """
    Generate a daily sequence of datetime objects starting from a given date.
    
    Parameters:
    - start (str): The starting date in the format 'yyyy-mm-dd'.
    - n (int): The number of datetime objects to generate.
    
    Returns:
    - list: A list of n datetime objects starting from the given date.
    """
    if not isinstance(start, str):
        raise TypeError("start must be a string.")
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    
    start_date = datetime.strptime(start, '%Y-%m-%d')
    date_sequence = [start_date + timedelta(days=i) for i in range(n)]
    
    return date_sequence




def add_date_range(values, start_date):
    """
    Add a date field to a sequence of values.
    
    Parameters:
    - values (list): A daily sequence of numerical values.
    - start_date (str): The start date in the format 'yyyy-mm-dd'.
    
    Returns:
    - list: A list containing tuple elements where each element contains (date, value).
    """
    date_sequence = date_range(start_date, len(values))
    result = list(zip(date_sequence, values))
    return result


import csv
from collections import defaultdict

def fees_report(infile, outfile):
    """
    Calculate late fees for each account and write a summary report in CSV form.
    
    Parameters:
    - infile (str): The path to the input CSV file.
    - outfile (str): The path to the output CSV file.
    """
    late_fees_by_patron = defaultdict(float)

    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date_returned = datetime.strptime(row['date_returned'], '%m/%d/%y')
            date_due = datetime.strptime(row['date_due'], '%m/%d/%Y')
            if date_returned > date_due:
                late_days = (date_returned - date_due).days
                late_fee = late_days * 0.25
                late_fees_by_patron[row['patron_id']] += late_fee

    with open(outfile, 'w', newline='') as csvfile:
        fieldnames = ['patron_id', 'late_fees']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for patron_id, late_fees in late_fees_by_patron.items():
            writer.writerow({'patron_id': patron_id, 'late_fees': '{:.2f}'.format(late_fees)})
