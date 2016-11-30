'''Functions for importing, exporting, transforming, and ecoding CSV file data.'''
import csv, base64, json

def jsonify(i_file):
    ''' Convert CSV file into JSON-style python object (list of dictionaries with keys as columns)
    returns: JSON-list object and column names (as a tuple). Column names are returns so that their order can be referenced later
    '''
    d_file = csv.DictReader(i_file)
    fieldnames = d_file.fieldnames
    return [row for  row in d_file], fieldnames

def generate_csv(file_name, d_list, fieldnames):
    '''
    Creates csv file from list of dictionaries (JSON_format)

    param file_name (string): File path
    param d_list (list): Data as list of dictionaries
    param fieldnames (list): List of column names to preserve column order
    returns: None
    '''
    with open(file_name, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames = fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(d_list)

def encode_json(j):
    '''Input JSON (list of dictionaries), output its B64 encoding'''
    s = json.dumps(j)
    b = s.encode('utf-8')
    b_6_4 = base64.b64encode(b)
    return b_6_4.decode('utf-8')

def transform_columns (data, fn, target_columns ):
    '''
    Meta-function that transforms JSON data in place by operating callbuck function on target column.

    param data (list): CSV data as JSON (list of dictionaries)
    param fn (function): Callback function with single argument to transform data.
    param target_columns(list or string): Column(s) to be transformed. Can be a list of columns or a string representing a single column.
    returns: data object (now transformed, probably)
    '''
    if isinstance(target_columns, str):
        target_columns = [target_columns]
    for record in data:
        for column in target_columns:
            record[column] = fn(record[column])
    return data
# note: can be modified to return list of corresponding elements in original data
def filter_out_rows(data, test_fn, target_columns):
    '''
    Meta-function that modifies JSON data in place by removing specified rows.

    param data (list): CSV data as JSON (list of dictionaries)
    param test_fn: (function): Callback function with single argument that returns Boolean. Boolean will indicate whether record will be removed.
    param target_columns(list or string): Column(s) to be targeted by test_fn. Can be a list of columns or a string representing a single column.
    returns: list of removed records
    '''
    if isinstance(target_columns, str):
        target_columns = [target_columns]
    new_list, removed_elements  = [], []
    for row in data:
        for column in target_columns:
            if test_fn(row[column]):
                removed_elements.append(row)
                break
        else:
            new_list.append(row)
    data[:] = new_list
    return removed_elements
