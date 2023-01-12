import csv


def read_user_values(id_):
    with open(f'values_{id_}.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=' ', skipinitialspace=False)
        array = []
        for line in file_reader:
            array.append(line)
        return array


def recording_user_values(array, id_):
    with open(f'values_{id_}.csv', 'w', encoding='utf-8') as file:
        for text in array:
            file.writelines(f'{text}\n')








# def read_index_row_data():
#     with open('index_row_data.csv', 'r', encoding='utf-8') as csvfile:
#         file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
#         for line in file_reader:
#             index_row = line
#         return index_row
#
# def recording_value_row_data(index_row):
#     with open(f'index_row_data.csv', 'w', encoding='utf-8') as file:
#         file.writelines(f'{index_row}\n')