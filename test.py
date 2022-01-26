from logg_decorator import logger_path
from constants import *


@logger_path(file_directory, file_name)
def data(a, b):
    return a * b


y = data(77, 77)
c = data(88, 88)
u = data(56, 70)
x = data(425, 89)
v = data(10, 78)




