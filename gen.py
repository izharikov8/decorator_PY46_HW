from constants import *
from logg_decorator import logger_path

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


@logger_path(file_directory, file_name)
def list_of_lists(my_list):
    for el in my_list:
        for el2 in el:
            yield el2


for item in list_of_lists(nested_list):
    print(item)