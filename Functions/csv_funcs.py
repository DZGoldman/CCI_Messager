import csv, base64,

def generate_csv(file_name, d_list, fieldnames):
    with open(file_name, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames = fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(d_list)

def encode_csv (path):
    with open(path, 'r') as f:
        s = f.read().encode('utf-8')
        b = base64.b64encode(s)
    return b


def transform_columns (data, fn, target_columns ):
    if isinstance(target_columns, str):
        target_columns = [target_columns]
    for record in data:
        for column in target_columns:
            record[column] = fn(record[column])
    return data
# note: can be modified to return list of corresponding elements in original data
def filter_out_rows(data, test_fn, target_columns):
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
